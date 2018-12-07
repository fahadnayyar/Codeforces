n=int(input())
x=list(map(int,input().split()))
for i in range(n):
	if i ==0:
		print(x[1]-x[0],x[n-1]-x[0])
	elif i==n-1:
		print(x[n-1]-x[n-2],x[n-1]-x[0])
	else:
		print(min(x[i]-x[i-1],x[i+1]-x[i]),max(x[n-1]-x[i],x[i]-x[0]))		
