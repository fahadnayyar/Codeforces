a=list(map(int,input().split()))
n=a[0]
m=a[1]
k=1
while n!=0:
	if k%m!=0:
		n=n-1
	k+=1
print(k-1)		