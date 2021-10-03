from __future__ import annotations
from collections.abc import Callable
import random
import sys
import math
import time

from _emerge.search import search


def bubble_sort(data: list[int]) -> int:
    steps = 0
    done = False

    while done is False:
        done = True
        for idx in range(1, len(data)):
            steps += 1
            if data[idx - 1] > data[idx]:
                done = False
                data[idx - 1], data[idx] = data[idx], data[idx - 1]
    return steps


def recursive_bubble_sort(data: list[int]) -> int:
    steps = 0
    done = True

    for idx in range(1, len(data)):
        steps += 1
        if data[idx - 1] > data[idx]:
            done = False
            data[idx - 1], data[idx] = data[idx], data[idx - 1]
    if not done:
        steps += recursive_bubble_sort(data)
    return steps


def selection_sort(data: list[int]) -> int:
    steps = 0
    data_len = len(data)
    current_elm = 0

    for idx in range(data_len):
        steps += 1
        min_idx = current_elm
        for search in range(current_elm + 1, data_len):
            steps += 1
            if data[min_idx] > data[search]:
                min_idx = search
        data[current_elm], data[min_idx] = data[min_idx], data[current_elm]
        current_elm += 1
    return steps


def insert_sort(data: list[int]) -> int:
    steps = 0
    for index in range(1, len(data)):
        steps += 1
        current_value = data[index]
        current_position = index

        while current_position > 0 and data[current_position - 1] > current_value:
            steps += 1
            data[current_position] = data[current_position - 1]
            current_position -= 1
        data[current_position] = current_value
    return steps


def quick_sort(data: list[int]) -> int:
    def _partition(array, p, r):
        x = array[r]
        i = p - 1
        for j in range(p, r):
            if array[j] <= x:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

    def _quicksort(array, first, last):
        steps = 0
        if first < last:
            q = _partition(array, first, last)
            steps += last - first
            steps += _quicksort(array, first, q - 1)
            steps += _quicksort(array, q + 1, last)
        return steps

    return _quicksort(data, 0, len(data) - 1)



def test_sort(sort_function: Callable[list[int]], sort_name: str):
    print("\nTesting %s:" % sort_name)
    print("  on random data: sorted with %d steps" % (sort_function(list(data))))
    print("  on sorted data: sorted with %d steps\n" % (sort_function(list(sorted_data))))
    start_time = time.monotonic()
    try:
        sort_function(list(big_data))
        print("  Time on %d random elements: %fs" % (BIG_SET, time.monotonic() - start_time))
    except RecursionError as e:
        print("  Time on %d random elements: DNF (%s)" % (BIG_SET, str(e)))


SIZE = 16
BIG_SET = 5000

if __name__ == "__main__":

    if len(sys.argv) > 1:
        try:
            SIZE = int(sys.argv[1])
        except:
            print("Invalid values %s:\nUsage: list_searches [list_size] [max_value]" % str(sys.argv[1:]))
            sys.exit(1)

    print("Creating list from a range 0,%d \n" % SIZE)

    sorted_data = list(range(0, SIZE))
    data = list(range(0, SIZE))
    random.shuffle(data)
    big_data = list(range(BIG_SET))
    random.shuffle(big_data)

    print("Sorting list of %d elements from 0 to %d" % (SIZE, SIZE))
    print(" [ O(n log %d) = %d ]\n\n" % (SIZE, SIZE * math.log2(SIZE)))

    test_sort(bubble_sort, "Bubble sort")
    test_sort(recursive_bubble_sort, "Recursive Bubble sort")
    test_sort(selection_sort, "Selection sort")
    test_sort(insert_sort, "Insert sort")
    test_sort(quick_sort, "Quick sort")








