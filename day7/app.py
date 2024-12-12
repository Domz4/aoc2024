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

    # Try all possible combinations of + and * in part 2 also || (concat)
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


#### solution part 2


def concat_number(a, b):
    # it's probaly faster doing it by math but i don't know how I can get lenght of a number ...
    return int(str(int(a)) + str(int(b)))


def evaluate_expression_with_concat(numbers, operators):
    res = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            res += numbers[i + 1]
        elif op == "||":
            res = concat_number(res, numbers[i + 1])
        elif op == "*":
            res *= numbers[i + 1]

    return res


def find_tenary_combinations(target, numbers):
    if len(numbers) == 1:
        return target == numbers[0]

    num_operators_needed = len(numbers) - 1

    for i in range(3**num_operators_needed):
        operators = []
        temp = i

        for _ in range(num_operators_needed):
            # changed this to generate 0, 1, 2
            rem = temp % 3
            if rem == 0:
                operators.append("+")
            elif rem == 1:
                operators.append("*")
            elif rem == 2:
                operators.append("||")

            temp //= 3

        res = evaluate_expression_with_concat(numbers, operators)

        if res == target:
            return True

    return False


def parse_line(line):
    parts = line.strip().split(":")
    target = int(parts[0])
    numbers = [int(x) for x in parts[1].strip().split()]
    return target, numbers


def solution2(input_text):
    total = 0

    for line in input_text.strip().split("\n"):
        if not line.strip():
            continue
        target, numbers = parse_line(line)
        if find_tenary_combinations(target, numbers):
            total += target

    return total


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:
        content = file.read()

    TEST_INPUT = """190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20"""

    # result = solution2(TEST_INPUT)
    result = solution2(content)
    print(result)
