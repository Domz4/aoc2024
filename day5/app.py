def solution(rules, instructions):
    result = 0

    for instruction in instructions:
        is_correct = True

        # precompute indices of all elements in the current instruction
        index_map = {num: idx for idx, num in enumerate(instruction)}

        for rule in rules:
            a, b = rule

            if a in index_map and b in index_map:
                if index_map[a] > index_map[b]:
                    is_correct = False
                    break

        if is_correct:
            result += instruction[len(instruction) // 2]

    return result


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()

    test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
    """  # output -> 143

    first_part, second_part = content.strip().split("\n\n")
    tuples_list = [
        tuple(map(int, line.split("|"))) for line in first_part.strip().split("\n")
    ]

    arrays_list = [
        list(map(int, line.split(","))) for line in second_part.strip().split("\n")
    ]

    print(solution(tuples_list, arrays_list))

# """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
#     """
