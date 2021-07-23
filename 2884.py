h,m = map(int,input().split())
m -= 45

if m>60:
    m -= 60
    h += 1
elif m<0:
    m += 60
    h -= 1

if h>24:
    h -= 24
elif h<0:
    h += 24

print(h,m)

'''best
h,m = map(int,input().split())
print((h-(m<45))%24,(b-45)%60)
'''