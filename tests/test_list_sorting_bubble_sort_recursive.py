import pytest

from algos import list_sorting

given = pytest.mark.parametrize


def test_recursive_bubble_sort_retval():
    test = [7]
    steps = list_sorting.recursive_bubble_sort(test)
    assert type(steps) is int
    assert type(test) is list
    assert len(test) == 1


def test_recursive_bubble_sort():
    test = [7, 6, 4]
    contrast = [4, 6, 7]
    _ = list_sorting.recursive_bubble_sort(test)
    assert test == contrast


def test_recursive_bubble_sort_empty():
    test = []
    _ = list_sorting.recursive_bubble_sort([])
    assert len(test) == 0
