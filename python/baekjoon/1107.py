n = int(input())
m = int(input())

if m == 0:
    buttons = []
else:
    buttons = list(map(int, input().split()))

result = abs(100 - n)

for i in range(999999):
    num = str(i)

    for j in num:
        if int(j) in buttons:
            break
    else:
        result = min(result, abs(n - i) + len(num))

print(result)
