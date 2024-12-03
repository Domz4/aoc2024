import re


def solution(inp: str):
    matches = re.findall("mul\(\d+,\d+\)", inp)
    result = 0
    for match in matches:
        n = re.findall(r"\d+", match)
        result += int(n[0]) * int(n[1])
    return result


def solution2(inp: str):
    matches = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", inp)
    result = 0
    indicator = "do()"

    for match in matches:
        if match == "do()" or match == "don't()":
            indicator = match
        else:
            if indicator == "do()":
                n = re.findall(r"\d+", match)
                result += int(n[0]) * int(n[1])

    return result


if __name__ == "__main__":

    with open("input.txt") as file:
        content = file.read()

    test_input = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    test_input2 = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )

    # print(solution(content))
    print(solution2(content))
