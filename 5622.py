#다이얼
alp = "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"
num = input()
enter = 0
for i in num:
    for j in range(len(alp)):
        if i in alp[j]:
            enter = enter + j+3

print(enter)
