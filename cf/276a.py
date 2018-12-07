yo=list(map(int,input().split()))
n=yo[0]
k=yo[1]
maxa=-(10**10)
for i in range(n):
	x=list(map(int,input().split()))
	if x[1]>k:
		ro=x[0]-(x[1]-k)
	else:
		ro=x[0]
	if ro>maxa:
		maxa=ro
print(maxa)				