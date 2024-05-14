def solution(land):
    n = len(land) # n x m 행렬
    m = len(land[0])
    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 여부를 저장하는 2차원 리스트
    result = [0 for _ in range(m)]  # 각 열에서 얻을 수 있는 석유량을 저장
    answer = 0

    for i in range(n):
        for j in range(m):
            # 석유가 있고 아직 방문하지 않았으면 BFS 탐색
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j, visited, n, m, land, result)

    answer = max(result)

    return answer

def bfs(x, y, visited, n, m, land, result):
    queue = [(x, y)]
    visited[x][y] = True  # 방문 표시
    amount = 0  # 석유가 있는 영역의 크기
    startY, endY = float('inf'), float('-inf')  # 석유가 있는 곳의 열의 범위

    # 큐가 빌 때까지 BFS를 수행
    while queue:
        cx, cy = queue.pop(0)  # 큐에서 data 하나 pop
        amount += 1  # 석유가 있는 영역의 크기를 증가
        startY, endY = min(startY, cy), max(endY, cy)  # 석유가 있는 곳의 열의 범위 update

        # 상하좌우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = cx + dx
            ny = cy + dy

            # 석유가 있고 아직 방문하지 않았다면 큐에 추가
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    # 얻을 수 있는 석유량을 result에 저장
    for col in range(startY, endY + 1):
        result[col] += amount
