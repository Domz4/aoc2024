from typing import List


def solution(reports: List[List[int]]):
    result = []
    for report in reports:
        # True if acending False if descending
        is_safe = True

        if report:
            indicator = "asc" if report[0] < report[1] else "desc"

            for i in range(len(report) - 1):
                temp = report[i] - report[i + 1]

                if abs(temp) > 3:
                    result.append(0)
                    is_safe = False
                    break

                if (
                    indicator == "desc"
                    and temp <= 0
                    or indicator == "asc"
                    and temp >= 0
                ):
                    result.append(0)
                    is_safe = False
                    break

            if is_safe:
                result.append(1)

    return sum(result)


def solution2(reports: List[List[int]]) -> int:
    def is_safe(series):
        if series:
            if len(series) < 2:
                return True

            is_increasing = None
            for i in range(1, len(series)):
                diff = series[i] - series[i - 1]

                if abs(diff) < 1 or abs(diff) > 3:
                    return False

                if is_increasing is None:
                    is_increasing = diff > 0
                elif (diff > 0) != is_increasing:
                    return False

            return True
        return False

    def is_safe_with_dampener(report):
        if is_safe(report):
            return True
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            if is_safe(modified_report):
                return True

        return False

    return sum(1 for report in reports if is_safe_with_dampener(report))


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read().split("\n")
        parsed_input = [[int(number) for number in c.split()] for c in content]

    test_input = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    # print(solution(parsed_input))
    print(solution2(parsed_input))
