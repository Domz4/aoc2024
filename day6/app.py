from __future__ import annotations


def solution(inp):
    directions = {
        "^": (-1, 0, ">"),
        ">": (0, 1, "v"),
        "v": (1, 0, "<"),
        "<": (0, -1, "^"),
    }

    # Parse the input to find the initial guard position and state
    rows, cols = len(inp), len(inp[0])
    guard_state = None
    guard_pos = None

    for i, row in enumerate(inp):
        for j, char in enumerate(row):
            if char in directions:
                guard_state = char
                guard_pos = (i, j)
                break
        if guard_state:
            break

    # Track visited positions
    visited = set()

    while True:
        visited.add(guard_pos)
        dy, dx, next_state = directions[guard_state]
        ny, nx = guard_pos[0] + dy, guard_pos[1] + dx

        # Check if the next position is out of bounds
        if not (0 <= ny < rows and 0 <= nx < cols):
            break

        # Check if the next position is an obstacle
        if inp[ny][nx] == "#":
            guard_state = next_state  # Turn  90deg
        else:
            inp[guard_pos[0]][guard_pos[1]] = "X"  # Mark visited
            guard_pos = (ny, nx)  # Move forward

    # Return the number of distinct positions visited
    return len(visited)


def count_obstruction_positions(grid):
    from copy import deepcopy

    directions = {
        "^": (-1, 0, ">"),
        ">": (0, 1, "v"),
        "v": (1, 0, "<"),
        "<": (0, -1, "^"),
    }

    def simulate_with_obstacle(grid, obstacle_pos):
        grid = deepcopy(grid)
        rows, cols = len(grid), len(grid[0])

        # Place the obstacle
        grid[obstacle_pos[0]][obstacle_pos[1]] = "O"

        # Find initial guard position and direction
        guard_state = None
        guard_pos = None

        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char in directions:
                    guard_state = char
                    guard_pos = (i, j)
                    break
            if guard_state:
                break

        visited = set()
        while True:
            # Add position and direction to visited set
            if (guard_pos, guard_state) in visited:
                return True  # Guard is in a loop
            visited.add((guard_pos, guard_state))

            dy, dx, next_state = directions[guard_state]
            ny, nx = guard_pos[0] + dy, guard_pos[1] + dx

            # Check if the next position is out of bounds
            if not (0 <= ny < rows and 0 <= nx < cols):
                return False

            # Check if the next position is an obstacle
            if grid[ny][nx] in ("#", "O"):
                guard_state = next_state  # Turn 90 degrees clockwise
            else:
                guard_pos = (ny, nx)  # Move forward

    rows, cols = len(grid), len(grid[0])
    count = 0

    # Try placing an obstacle at each empty position
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                if simulate_with_obstacle(grid, (i, j)):
                    count += 1

    return count


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as file:
        content = file.read()

    # guard is at ^, obstacles are at #
    # guard states | up: ^, down: v, left: <, right: >

    test_input = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """  # output -> 41

    ###################### change input -->
    parsed_input = [list(line) for line in content.split()]

    print(count_obstruction_positions(parsed_input))
