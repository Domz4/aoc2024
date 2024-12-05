def find_xmas_instances(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def check_word(row, col, dx, dy):

        # check the bouds
        if not (0 <= row + 3 * dx < rows and 0 <= col + 3 * dy < cols):
            return False

        word = ""
        for i in range(4):
            word += grid[row + i * dx][col + i * dy]
        return word == "XMAS"

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1

    return count


def find_mas_instances(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Check only diagonals
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            M = grid[i][j]

            if M != "A":
                continue

            TL = grid[i - 1][j - 1]  # Top Left
            TR = grid[i - 1][j + 1]  # Top Right
            BL = grid[i + 1][j - 1]  # Bottom Left
            BR = grid[i + 1][j + 1]  # Bottom Right

            diag1 = TL + M + BR
            diag2 = TR + M + BL

            if diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM"):
                count += 1

            print("diag1", diag1)
            print("diag2", diag2)
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()

    test_nums = [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ]
    test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".split()

    print(find_mas_instances(content.split()))
