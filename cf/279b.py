yo=list(map(int,input().split()))
n=yo[0];
t=yo[1];
a=list(map(int,input().split()))
arr=[]

for i in range(n):
	add=0
	for j in range(i,n,1):
		add+=a[j]
		if add>t:
			arr.append(j-i)
			break
		elif add==t:
			arr.append(j-i+1)
			break
		elif j==n-1:
			arr.append(j-i+1)	
#print(arr)
ans=max(arr)
print(ans)			
