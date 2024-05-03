import sys
sys.setrecursionlimit(10**6)  # 런타임 에러 안뜨게 하려면 이거 넣어야 함

# 좌표 변화량
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, table, m, n):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and table[ny][nx] == 1:
            table[ny][nx] = 0
            dfs(nx, ny, table, m, n)
                
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    table = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        table[y][x] = 1
    for x in range(m):
        for y in range(n):
            if table[y][x] == 1:
                dfs(x, y, table, m, n)
                count += 1
    print(count)
