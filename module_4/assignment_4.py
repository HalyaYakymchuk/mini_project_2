"""third task"""

import bisect

# def solve_2sum_basic(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         nums_set = set(int(line.strip()) for line in file)

#     nums_list = list(nums_set)
#     found_targets = set()

#     T_MIN = -10000
#     T_MAX = 10000

#     for x in nums_list:
#         for t in range(T_MIN, T_MAX + 1):
#             y = t - x
#             if y in nums_set and y != x:
#                 found_targets.add(t)

#     return len(found_targets)

def solve_2sum_basic(filename):
    """Calculates the number of unique target values t in the range [-10000, 10000]
    that can be expressed as the sum of two distinct numbers from the input file."""

    with open(filename, "r", encoding="utf-8") as file:
        nums_set = sorted(set(int(line.strip()) for line in file))

    found_targets = set()
    T_MIN = -10000
    T_MAX = 10000
    n = len(nums_set)

    for x in nums_set:
        y_low = T_MIN - x
        y_high = T_MAX - x

        idx_low = bisect.bisect_left(nums_set, y_low)
        idx_high = bisect.bisect_right(nums_set, y_high)

        for i in range(idx_low, idx_high):
            y = nums_set[i]
            if x != y:
                found_targets.add(x + y)
    return len(found_targets)


print(solve_2sum_basic("test4.txt"))
