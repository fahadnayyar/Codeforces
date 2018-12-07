n=int(input())
a=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
lis=[]
for i in range(n):
	#print(lis)
	if i==0:
		yo=[1,a[0]]
		lis.append(yo)
	else:
		#print(i)
		#print(lis[i-1][1])

		yo=[lis[i-1][1]+1,lis[i-1][1]+a[i]]	
		lis.append(yo)
#print(lis)		

for j in q:
	for t in range(n):
		if lis[t][0]<=j<=lis[t][1]:
			print(t+1)
			break