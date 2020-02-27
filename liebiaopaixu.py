n=int(input())
a=input("")
num=[int(n) for n in a.split()]
num.sort()
for i in range(n):
    y=num[i]
    print(y,end=' ')
