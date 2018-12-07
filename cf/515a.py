t=list(map(int,input().split()))
a=t[0]
b=t[1]
s=t[2]
yo=abs(a)+abs(b)
ro=s-yo
if ro<0:
	print('No')
elif ro%2==0:
	print('Yes')
else:
	print('No')		