from math import ceil
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#a=list(map(int,input().split()))
n=int(input())
a=a[0]+a[1]+a[2]
b=b[0]+b[1]+b[2]
a=ceil(a/5)
b=ceil(b/10)
if a+b<=n:
	print('YES')
else:
	print('NO')	