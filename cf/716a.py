p=list(map(int,input().split()))
n=p[0]
c=p[1]
q=list(map(int,input().split()))
count=1
for i in range(n-1):
	if q[i+1]-q[i]>c:
		count=1
	else:
		count+=1
print(count)			