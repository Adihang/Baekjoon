#알파벳 넘버
alp = "abcdefghijklmnopqrstuvwxyz"
word = input()
num = list()
for i in alp:
    num.append(word.find(i))
    
print(*num)
