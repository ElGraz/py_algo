from __future__ import annotations

import math
import random
import sys
from typing import Tuple


def binary_search(needle: int, haystack: list[int]) -> Tuple[bool, int]:
    steps = 0

    left = 0
    right = len(haystack) - 1
    mid = int((right + left) / 2)

    while left <= right:
        steps += 1
        if haystack[mid] == needle:
            return True, steps
        if haystack[mid] > needle:
            right = mid - 1
        else:
            left = mid + 1
        mid = int((right + left) / 2)

    return False, steps


def jump_search(needle: int, haystack: list[int]) -> Tuple[bool, int]:
    steps = 0
    data_len = len(haystack)
    # Finding block size to be jumped
    step = math.sqrt(data_len)

    # Finding the block where element is
    # present (if it is present)
    prev = 0.0
    while haystack[int(min(step, data_len) - 1)] < needle:
        steps += 1
        prev = step
        step += step
        if prev >= needle:
            return False, steps

    # Doing a linear search for x in
    # block beginning with prev.
    while haystack[int(prev)] < needle:
        steps += 1
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, data_len):
            return False, steps

    # If element is found
    if haystack[int(prev)] == needle:
        return True, steps

    return False, steps


def is_found(value):
    if value:
        return ""
    return "*not*"


if __name__ == "__main__":
    SIZE = 16
    CONCENTRATION = 1

    if len(sys.argv) > 1:
        try:
            SIZE = int(sys.argv[1])
            CONCENTRATION = int(sys.argv[2])
        except ValueError:
            print(
                "Invalid values %s:\n"
                "Usage: list_searches [list_size] [max_value]"
                % str(sys.argv[1:])
            )
            sys.exit(1)

        print("Creating list from a range 0,%d \n" % SIZE)

    data = random.sample(list(range(0, SIZE * CONCENTRATION)), SIZE)
    data.sort()

    NEEDLE = data[random.randint(0, len(data) - 1)]
    NOT_NEEDLE = (SIZE * CONCENTRATION) * 2

    print(
        "Searching for %d in an ordered list of size %d from 0 to %d"
        % (NEEDLE, SIZE, SIZE * CONCENTRATION)
    )
    print(" [ O(log %d) = %d ]\n\n" % (SIZE, math.log2(SIZE)))

    (found, steps) = binary_search(NEEDLE, data)
    print(
        "Binary search: %d has %s been found with %d steps"
        % (NEEDLE, is_found(found), steps)
    )
    (found, steps) = binary_search(NOT_NEEDLE, data)
    print(
        "Binary search: %d has %s been found with %d steps"
        % (NOT_NEEDLE, is_found(found), steps)
    )

    print("")

    (found, steps) = jump_search(NEEDLE, data)
    print(
        "Jump search: %d has %s been found with %d steps"
        % (NEEDLE, is_found(found), steps)
    )
    (found, steps) = jump_search(NOT_NEEDLE, data)
    print(
        "Jump search: %d has %s been found with %d steps"
        % (NOT_NEEDLE, is_found(found), steps)
    )
