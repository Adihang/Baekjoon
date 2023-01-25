#문자열 반복
num = int(input())
for i in range(num):
    word = input().split()
    n = ""
    for i in str(word[1]):
        n += i * int(word[0])
    print(n)
