from __future__ import annotations
from collections import deque


def solution(rules, instructions):
    result = 0

    for instruction in instructions:
        is_correct = True

        # precompute indices of all elements in the current instruction
        index_map = {num: idx for idx, num in enumerate(instruction)}

        # print(index_map)

        for rule in rules:
            a, b = rule

            if a in index_map and b in index_map:
                if index_map[a] > index_map[b]:
                    is_correct = False
                    break

        if is_correct:
            result += instruction[len(instruction) // 2]

    return result


def solution2(rules, instructions):
    def is_valid(rules, sequence):
        for a, b in rules:
            if a in sequence and b in sequence:
                if sequence.index(a) > sequence.index(b):
                    return False
        return True

    def dfs(graph, v, stack, visited):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(graph, neighbor, stack, visited)
        stack.appendleft(v)

    def topsort(tuple_list):
        nodes = set(node for edge in tuple_list for node in edge)
        graph = {node: [v for u, v in tuple_list if u == node] for node in nodes}
        stack = deque()
        visited = set()
        for v in graph:
            if v not in visited:
                dfs(graph, v, stack, visited)
        return stack

    result = 0
    for instruction in instructions:
        if not is_valid(rules, instruction):
            relevant_rules = [
                (a, b) for a, b in rules if a in instruction and b in instruction
            ]
            order = topsort(relevant_rules)
            reordered = [page for page in order if page in instruction]
            # Find the middle element
            mid = len(reordered) // 2
            result += reordered[mid]

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
    """  # output -> 143, part1 | output -> 123, part2

    first_part, second_part = content.strip().split("\n\n")

    tuples_list = [
        tuple(map(int, line.split("|"))) for line in first_part.strip().split("\n")
    ]

    arrays_list = [
        list(map(int, line.split(","))) for line in second_part.strip().split("\n")
    ]

    print(solution2(tuples_list, arrays_list))
    # print(solution(tuples_list, arrays_list))
