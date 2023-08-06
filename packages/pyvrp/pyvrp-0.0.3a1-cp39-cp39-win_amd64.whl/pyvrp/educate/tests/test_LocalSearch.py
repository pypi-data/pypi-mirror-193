from numpy.testing import assert_, assert_equal, assert_raises
from pytest import mark

from pyvrp import Individual, PenaltyManager, XorShift128
from pyvrp.educate import LocalSearch, NeighbourhoodParams, compute_neighbours
from pyvrp.tests.helpers import read


def test_local_search_raises_when_there_are_no_operators():
    data = read("data/OkSmall.txt")
    pm = PenaltyManager(data.vehicle_capacity)
    rng = XorShift128(seed=42)

    ls = LocalSearch(data, pm, rng)
    individual = Individual(data, pm, rng)

    with assert_raises(RuntimeError):
        ls.search(individual)

    with assert_raises(RuntimeError):
        ls.intensify(individual)


def test_local_search_raises_when_neighbourhood_structure_is_empty():
    data = read("data/OkSmall.txt")
    pm = PenaltyManager(data.vehicle_capacity)
    rng = XorShift128(seed=42)

    ls = LocalSearch(data, pm, rng)
    ls.set_neighbours([[] for _ in range(data.num_clients + 1)])

    individual = Individual(data, pm, rng)

    with assert_raises(RuntimeError):
        ls.search(individual)


@mark.parametrize(
    "weight_wait_time,"
    "weight_time_warp,"
    "nb_granular,"
    "symmetric_proximity,"
    "symmetric_neighbours",
    [
        (20, 20, 10, True, False),
        (20, 20, 10, True, True),
        # From original c++ implementation
        # (18, 20, 34, False),
        (18, 20, 34, True, True),
    ],
)
def test_local_search_set_get_neighbours(
    weight_wait_time: int,
    weight_time_warp: int,
    nb_granular: int,
    symmetric_proximity: bool,
    symmetric_neighbours: bool,
):
    data = read("data/RC208.txt", "solomon", round_func="trunc")

    seed = 42
    rng = XorShift128(seed=seed)
    pen_manager = PenaltyManager(data.vehicle_capacity)
    ls = LocalSearch(data, pen_manager, rng)

    params = NeighbourhoodParams(
        weight_wait_time,
        weight_time_warp,
        nb_granular,
        symmetric_proximity,
        symmetric_neighbours,
    )
    neighbours = compute_neighbours(data, params)

    # Test that before we set neighbours we don't have same
    assert_(ls.get_neighbours() != neighbours)

    # Test after we set we have the same
    ls.set_neighbours(neighbours)
    ls_neighbours = ls.get_neighbours()
    assert_equal(ls_neighbours, neighbours)

    # Check that the bindings make a copy (in both directions)
    assert_(ls_neighbours is not neighbours)
    ls_neighbours[1] = []
    assert_(ls.get_neighbours() != ls_neighbours)
    assert_equal(ls.get_neighbours(), neighbours)
    neighbours[1] = []
    assert_(ls.get_neighbours() != neighbours)
