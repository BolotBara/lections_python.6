# import random 
# massiv = [
#     ['x', 2, 5, 'x', 'x', 'x'], 
#     ['x', 'x', 6, 'x', 'x', 'x'], 
#     [6, 4, 'x', 'x', 'x', 2], 
#     [3, 'x', 'x', 'x', 1, 4], 
#     ['x', 'x', 'x', 1, 'x', 'x'], 
#     ['x', 'x', 'x', 'x', 'x', 'x']
# ]
# def zamena_x_na_random(a, b = 1, c = 7):    
#     for inner in a:
#         for i in range(len(inner)):
#             if inner[i] == 'x':
#                 inner[i] = random.randint(b, c) 

# zamena_x_na_random(massiv)
# for i in massiv:
#     print(i)

# def is_valid_sudoku(matrix):

#     for i in range(6):
#         row_values = set()
#         col_values = set()
#         for j in range(6):
#             if matrix[i][j] != 'x' and matrix[i][j] in row_values:
#                 return False  
#             row_values.add(matrix[i][j])

#             if matrix[j][i] != 'x' and matrix[j][i] in col_values:
#                 return False  
#             col_values.add(matrix[j][i])

#     diagonal_values1 = set()
#     diagonal_values2 = set()
#     for i in range(6):
#         if matrix[i][i] != 'x' and matrix[i][i] in diagonal_values1:
#             return False 
#         diagonal_values1.add(matrix[i][i])

#         if matrix[i][5 - i] != 'x' and matrix[i][5 - i] in diagonal_values2:
#             return False  
#         diagonal_values2.add(matrix[i][5 - i])

#     return True  

# massiv = [
#     ['x', 2, 5, 'x', 'x', 'x'],
#     ['x', 'x', 6, 'x', 'x', 'x'],
#     [6, 4, 'x', 'x', 'x', 2],
#     [3, 'x', 'x', 'x', 1, 4],
#     ['x', 'x', 'x', 1, 'x', 'x'],
#     ['x', 'x', 'x', 'x', 'x', 'x']
# ]

# result = is_valid_sudoku(massiv)
# print(result)

# def is_valid_placement(matrix, row, col, num):

#     for i in range(6):
#         if matrix[row][i] == num or matrix[i][col] == num:
#             return False

#     start_row, start_col = 2 * (row // 2), 3 * (col // 3)
#     for i in range(start_row, start_row + 2):
#         for j in range(start_col, start_col + 3):
#             if matrix[i][j] == num:
#                 return False

#     return True

# def solve_sudoku(matrix):
#     for i in range(6):
#         for j in range(6):
#             if matrix[i][j] == 'x':
#                 for num in range(1, 7):
#                     if is_valid_placement(matrix, i, j, num):
#                         matrix[i][j] = num
#                         if solve_sudoku(matrix):
#                             return True
#                         matrix[i][j] = 'x'  
#                 return False  
#     return True  

# initial_sudoku = is_valid_sudoku(massiv)

# if initial_sudoku:

#     for i in range(6):
#         if massiv[i][i] == 'x':
#             massiv[i][i] = i + 1
#         if massiv[i][5 - i] == 'x':
#             massiv[i][5 - i] = 6 - i
#         if massiv[0][i] == 'x':
#             massiv[0][i] = i + 1
#         if massiv[5][i] == 'x':
#             massiv[5][i] = 6 - i
#         if massiv[i][0] == 'x':
#             massiv[i][0] = i + 1
#         if massiv[i][5] == 'x':
#             massiv[i][5] = 6 - i

#     solve_sudoku(massiv)

#     print("Решенное судоку:")
#     for row in massiv:
#         print(row)
# else:
#     print("Исходное судоку некорректное.")
