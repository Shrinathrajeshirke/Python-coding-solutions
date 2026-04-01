# > **Write a program that:**
# > - Creates a 2D list (3x3 matrix)
# > - Prints it in matrix format
# > - Prints sum of each row
# > - Prints the diagonal elements


def matrix_ops():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matrix: ")
    
    for row in matrix:
        for element in row:
            print(element, end= " ")
        print()

    print("Row Sums: ")
    for i,row in enumerate(matrix):
        print(f"Row {i+1}: {sum(row)}")

    diagonal_elements = []
    for i, row in enumerate(matrix):
        for j,element in enumerate(row):
            if i==j:
                diagonal_elements.append(element)
    
    print(f"Diagonal: {diagonal_elements}")

matrix_ops()