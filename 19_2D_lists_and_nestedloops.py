
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(number_grid [3][1])
print("\n")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
for row in number_grid:
    for col in row:
        print(col)
print("\n")

# 2D List: Classroom seating chart (rows x columns)
# Each inner list represents a row of seats with students' names
seating_chart = [
    ["Alice", "Bob", "Charlie"], # Row 1
    ["Diana", "Ethan", "Fiona"], # Row 2
    ["George", "Hannah", "Ian"]  # Row 3
]

#Start a nested loop using enumerate() to get both the row index and the row data
for row_index, row in enumerate(seating_chart):
    print(f"Row {row_index +1}:")  # Print the row number (row_index +1 because Python starts at 0 but seats usually start at 1)
    for student in row: # Inner loop: iterate through each student name inside the current row
        print(f"  Seat: {student}")