def solution(friends, gifts):
    dic = dict(zip(friends, range(len(friends)))) # friends list to dict
    table = [[0 for _ in friends] for _ in friends] # friends list 길이 기반 2차원 list 생성, 모든 값 0
    # table[i][j]는 i가 j에게 준 선물의 수
    presents = [0 for _ in friends]

    for gift in gifts:
        m, n = gift.split() # m = given, n = taken
        table[dic[m]][dic[n]] += 1 # m이 n에게 준 선물의 수 +1

    given = [sum(row) for row in table] # 행 계산 -> 준 선물의 개수
    taken = [sum(row[i] for row in table) for i in range(len(friends))] # 열 계산 -> 받은 선물의 개수
    exp = [given - taken for given, taken in zip(given, taken)] # 지수

    for i in range(len(friends)): # 나
        for j in range(i+1, len(friends)): # 너
            if table[i][j] > table[j][i]: # 내가 너에게 준 선물이 너가 나에게 준 선물보다 많을 때
                presents[i] += 1 # 나 + 1
            elif table[j][i] > table[i][j]: # 너가 나에게 준 선물이 내가 너에게 준 선물보다 많을 때
                presents[j] += 1 # 너 + 1
            else:
                if exp[i] > exp[j]: # 나의 지수가 너의 지수보다 클 때
                    presents[i] += 1 # 나 + 1
                if exp[j] > exp[i]: # 너의 지수가 나의 지수보다 클 때
                    presents[j] += 1 # 너 + 1
                    
    return max(presents)
