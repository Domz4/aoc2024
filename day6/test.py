# Example input
input_grid = [
    list("....#....."),
    list(".........#"),
    list(".........."),
    list("..#......."),
    list(".......#.."),
    list(".........."),
    list(".#..^....."),
    list("........#."),
    list("#........."),
    list("......#..."),
]

print(input_grid)
result = count_obstruction_positions(input_grid)
print("Number of valid obstruction positions:", result)
