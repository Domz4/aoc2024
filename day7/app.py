def evaluate_expression(numbers, operators):
    res = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            res += numbers[i + 1]
        else:
            res *= numbers[i + 1]
    return res


def find_valid_combinations(target, numbers):
    if len(numbers) == 1:
        return target == numbers[0]

    # we need n-1 operators
    num_operators_needed = len(numbers) - 1

    # Try all possible combinations of + and *
    for i in range(2**num_operators_needed):
        operators = []
        for j in range(num_operators_needed):
            if (i >> j) & 1:
                operators.append("+")
            else:
                operators.append("*")

        res = evaluate_expression(numbers, operators)
        if res == target:
            return True

    return False


def solution(input_text):
    total = 0

    for line in input_text.strip().split("\n"):
        if not line.strip():
            continue
        target, numbers = parse_line(line)
        if find_valid_combinations(target, numbers):
            total += target

    return total


def parse_line(line):
    parts = line.strip().split(":")
    target = int(parts[0])
    numbers = [int(x) for x in parts[1].strip().split()]
    return target, numbers


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()

    test_input = """190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20"""

    result = solution(content)
    print(result)
