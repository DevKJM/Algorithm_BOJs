repeat = int(input())
arr = []

for i in range(repeat):
    a,b =map(int,input().split())
    arr.append(a+b)

for j in range(0,repeat):
    print(arr[j])
