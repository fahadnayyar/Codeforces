n=int(input())
ans=0
mat=[]
for i in range(n):
	x=input()
	yo=x.count('C')
	ans+=(yo*(yo-1)//2)
	mat.append(x)
for i in range(n):
	count=0
	for j in range(n):
		if mat[j][i]=='C':
			count+=1
	ans+=(count*(count-1)//2)
print(ans)			
