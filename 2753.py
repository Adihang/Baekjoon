#윤년
i = int(input())
if (i%100)!=0 and (i%4)==0 :
    print (1)
elif (i%400)==0:
    print(1)
else :
    print(0)
