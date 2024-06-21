import heapq

n = int(input())

def sort_by_start_time(lecture):
    return lecture[1]

lectures = [list(map(int, input().split(" "))) for _ in range(n)]
lectures.sort(key=sort_by_start_time)

hq = []
heapq.heapify(hq)

count = 1
for i in range(n):
    if i != 0:
        while hq:
            if hq[0] > lectures[i][1]:
                break
            else:
                heapq.heappop(hq)
    heapq.heappush(hq, lectures[i][2])

    count = max(count, len(hq))

print(count)
