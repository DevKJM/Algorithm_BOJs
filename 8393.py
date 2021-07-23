'''
def sum(num,n):
    if n != 0:
        num += n
        return sum(num,n-1)
    return num

n = int(input())
print(sum(0,n))

# -- runtime error
'''

n = int(input())
arr = 0
for i in range(1,n+1):
    arr += i

print(arr)

# -- best
# n=int(input())
# print(int(n*(n+1)/2))

