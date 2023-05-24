# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# n = len(matrix)
# for i in range(n):
#     for j in range(i,n):
#         matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
# for i in range(n):
#     matrix[i] = matrix[i][::-1]
# for i in matrix:
#     print(*i)
# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
#
# diagonal_sum = sum(mat[i][i] for i in range(len(mat)))
#
# print(diagonal_sum)


# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# numRows = len(mat)
# numCols = len(mat[0])
# summ = 0
# for i in range(numRows):
#     for j in range(numCols):
#         if i == 0 or j == 0 or i == numRows - 1 or j == numCols - 1:
#             summ+=mat[i][j]
# print(summ)


# matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
# for i in range(len(matrix)-1):
#     for j in range(len(matrix[0])-1):
#         if matrix[i][j]!=matrix[i+1][j+1]:
#             return True
#         else:
#             return False

#
# board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
#          [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
# n = len(board)
# m = len(board[0])
# cnt = 0
# r = -1
# c = -1
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 'R':
#             r = j
#             c = j
#             break
#
# for i in range(r - 1):
#     if board[i][c] == 'p':
#         cnt += 1
#         break
#     if board[i][c] == 'B':
#         break
# for i in range(r + 1):
#     if board[i][c] == 'p':
#         cnt += 1
#         break
#     if board[i][c] == 'B':
#         break
# for j in range(c - 1):
#     if board[r][j] == 'p':
#         cnt += 1
#         break
#     if board[r][j] == 'B':
#         break
# for j in range(c + 1):
#     if board[r][j] == 'p':
#         cnt += 1
#         break
#     if board[r][j] == 'B':
#         break
# print(cnt)
# board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
#          [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
#          [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if board[i][j] == 'R':
#             x, y = i, j
#             break
# captures = 0
# for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#     i, j = x + dx, y + dy
#     while 0 <= i < len(board) and 0 <= j < len(board[0]):
#         if board[i][j] == 'p':
#             captures += 1
#             break
#         elif board[i][j] != '.':
#             break
#         i += dx
#         j += dy
#
# print(captures)
board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 'R':
            x, y = i, j
            break
res = 0
for j in range(y + 1, len(board[0])):
    if board[x][j] == 'p':
        res += 1
        break
    elif board[x][j] != '.':
        break
for j in range(y - 1, -1, -1):
    if board[x][j] == 'p':
        res += 1
        break
    elif board[x][j] != '.':
        break
for i in range(x + 1, len(board)):
    if board[i][y] == 'p':
        res += 1
        break
    elif board[i][y] != '.':
        break
for i in range(x - 1, -1, -1):
    if board[i][y] == 'p':
        res += 1
        break
    elif board[i][y] != '.':
        break
print(res)
