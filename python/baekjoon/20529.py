def distance(mbti): # 각 유형별로 비교 해서 다르면 거리를 1씩 증가하는 함수
    d = 0
    for i in range(4):
        d += mbti[0][i] != mbti[1][i]
        d += mbti[0][i] != mbti[2][i]
        d += mbti[1][i] != mbti[2][i]

    return d

for _ in range(int(input())): # 테스트 케이스 수(3명)
    N = int(input()) # 사람 수
    mbti = input().split() # 각 사람의 mbti

    if N > 32: # 9999집
        print(0)
    else:
        result = 12 # 최대 가능 거리를 default로 먼저 선언

        for i in range(N): # 열심히 비교해라
            for j in range(i+1, N):
                for k in range(j+1, N):
                    case = min(result, distance([mbti[i], mbti[j], mbti[k]]))
        print(result)
