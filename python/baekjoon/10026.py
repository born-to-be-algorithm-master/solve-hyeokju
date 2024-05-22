def bfs(matrix, x, y, color):
    queue = []
    queue.append((x, y))
    matrix[x][y] = 'X'
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        cur = queue.pop(0)
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == color:
                    queue.append((nx, ny))
                    matrix[nx][ny] = 'X'
    return 1


n = int(input().strip())
matrix = [list(input().strip()) for _ in range(n)]

# 색약 matrix 생성
ab_matrix = [row[:] for row in matrix]
for i in range(n):
    for j in range(n):
        if ab_matrix[i][j] == 'G':
            ab_matrix[i][j] = 'R'

normal_count = 0
abnormal_count = 0

# 일반
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G' or matrix[i][j] == 'B':
            if matrix[i][j] == 'X':
                continue
            normal_count += bfs(matrix, i, j, matrix[i][j])

# 색약
for i in range(n):
    for j in range(n):
          if ab_matrix[i][j] == 'R' or ab_matrix[i][j] == 'B':
            if ab_matrix[i][j] == 'X':
                continue
            abnormal_count += bfs(ab_matrix, i, j, ab_matrix[i][j])

print(normal_count, abnormal_count)
