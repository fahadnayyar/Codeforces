from math import ceil
t=list(map(int,input().split()))
n=t[0]
x=t[1]
c=list(map(int,input().split()))
yo=sum(c)
if abs(yo) <= abs(x):
	if yo==0:
		print(0)

	else:
		print(1)
else:	
	print(ceil(abs(yo)/x))
