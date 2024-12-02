from collections import defaultdict
from typing import List
import math


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:
        content = file.read().split()

        left_list = [int(num) for num in content[::2]]
        right_list = [int(num) for num in content[1::2]]

    test_l = [3, 4, 2, 1, 3, 3]
    test_r = [4, 3, 5, 3, 9, 3]

    def solution(l: List[int], r: List[int]):
        l.sort()
        r.sort()
        return sum(abs(xl - xr) for xl, xr in zip(l, r))

    def solution2(l: List[int], r: List[int]):
        values: dict[int, int] = defaultdict(lambda: 0)
        res = 0
        for n in r:
            if n in values:
                values[n] += 1
            else:
                values[n] = 1

        for item in l:
            res += item * values[item]

        return res

    print(solution(left_list, right_list))
    # print(solution2(test_l, test_r))
