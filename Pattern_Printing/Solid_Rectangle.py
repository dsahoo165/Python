# Get the number of rows from the user
row = int(input("Enter number of rows: "))

# Get the number of columns from the user
column = int(input("Enter number of columns: "))

# Loop to print the pattern
for i in range(1, row + 1):
    for j in range(1, column + 1):
        print("*", end="")
    print()
