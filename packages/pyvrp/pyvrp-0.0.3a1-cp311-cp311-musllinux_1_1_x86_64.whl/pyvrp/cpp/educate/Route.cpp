#include "Route.h"

#include <cmath>
#include <ostream>

void Route::setupNodes()
{
    nodes.clear();
    auto *node = depot;

    do
    {
        node = n(node);
        nodes.push_back(node);
    } while (!node->isDepot());
}

void Route::setupAngle()
{
    if (empty())
    {
        angleCenter = 1.e30;
        return;
    }

    int cumulatedX = 0;
    int cumulatedY = 0;

    for (auto it = nodes.begin(); it != nodes.end() - 1; ++it)
    {
        auto const *node = *it;
        assert(!node->isDepot());

        cumulatedX += data->client(node->client).x;
        cumulatedY += data->client(node->client).y;
    }

    // This computes a pseudo-angle that sorts roughly equivalently to the atan2
    // angle, but is much faster to compute. See the following post for details:
    // https://stackoverflow.com/a/16561333/4316405.
    auto const routeSize = static_cast<double>(size());
    auto const dy = cumulatedY / routeSize - data->depot().y;
    auto const dx = cumulatedX / routeSize - data->depot().x;
    angleCenter = std::copysign(1. - dx / (std::fabs(dx) + std::fabs(dy)), dy);
}

void Route::setupRouteTimeWindows()
{
    auto *node = nodes.back();

    do  // forward time window segments
    {
        auto *prev = p(node);
        prev->twAfter = TimeWindowSegment::merge(prev->tw, node->twAfter);
        node = prev;
    } while (!node->isDepot());
}

void Route::update()
{
    auto const oldNodes = nodes;
    setupNodes();

    int load = 0;
    int distance = 0;
    int reverseDistance = 0;
    bool foundChange = false;

    for (size_t pos = 0; pos != nodes.size(); ++pos)
    {
        auto *node = nodes[pos];

        if (!foundChange && (pos >= oldNodes.size() || node != oldNodes[pos]))
        {
            foundChange = true;

            if (pos > 0)  // change at pos, so everything before is the same
            {             // and we can re-use cumulative calculations
                load = nodes[pos - 1]->cumulatedLoad;
                distance = nodes[pos - 1]->cumulatedDistance;
                reverseDistance = nodes[pos - 1]->cumulatedReversalDistance;
            }
        }

        if (!foundChange)
            continue;

        load += data->client(node->client).demand;
        distance += data->dist(p(node)->client, node->client);

        reverseDistance += data->dist(node->client, p(node)->client);
        reverseDistance -= data->dist(p(node)->client, node->client);

        node->position = pos + 1;
        node->cumulatedLoad = load;
        node->cumulatedDistance = distance;
        node->cumulatedReversalDistance = reverseDistance;
        node->twBefore = TimeWindowSegment::merge(p(node)->twBefore, node->tw);
    }

    setupAngle();
    setupRouteTimeWindows();

    load_ = nodes.back()->cumulatedLoad;
    isLoadFeasible_ = static_cast<size_t>(load_) <= data->vehicleCapacity();

    timeWarp_ = nodes.back()->twBefore.totalTimeWarp();
    isTimeWarpFeasible_ = timeWarp_ == 0;
}

std::ostream &operator<<(std::ostream &out, Route const &route)
{
    out << "Route #" << route.idx + 1 << ":";  // route number
    for (auto *node = n(route.depot); !node->isDepot(); node = n(node))
        out << ' ' << node->client;  // client index
    out << '\n';

    return out;
}
