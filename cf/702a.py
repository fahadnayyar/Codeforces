n=int(input())
a=list(map(int,input().split()))
i=0

count=1
arr=[]
for i in range(n-1):
	if a[i+1]>a[i]:
		count+=1
		if i==n-2:
			arr.append(count)
	else:
		arr.append(count)
		count=1
	#print(count,i,a[i],arr)	
if arr==[]:
	print(1)
else:


	print(max(arr))			