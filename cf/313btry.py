s=input()
s=' '+s
n=int(input())
for k in range(n):
	query=list(map(int,input().split()))
	i=query[0]
	j=query[1]
	count=0
	for t in range(i+1,j+1):
		if s[t]==s[t-1]:
			count+=1
	print(count)		