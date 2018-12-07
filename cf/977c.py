x=list(map(int,input().split()))
n=x[0]
k=x[1]
arr=list(map(int,input().split()))
arr.sort()
#print(arr)
if k==0:
	yo=arr[0]-1
	if yo>=1:
		print(yo)
	else:
		print(-1)	
elif (k==n):
	print(arr[k-1])	
else:

	p=arr[k-1]
	q=arr[k]
	if p==q:
		print(-1)
	else:
		print(p)