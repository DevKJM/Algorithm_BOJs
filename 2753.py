#윤년 1 not 0

a = int(input())

if(a%4 == 0):
    if(a%400 == 0):
        print("1")
    elif(a%100 == 0):
        print("0")
    else:
        print("1")
else:
    print("0")

''' (best)
a = int(input())
if a%4==0 a%100!=0 or a%400==0:
    print(1)
else:
    print(0)
'''