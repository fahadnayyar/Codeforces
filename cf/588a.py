n=int(input())
ai=[]
pi=[]
for i in range (n):
	a=list(map(int,input().split()))
	ai.append(a[0])
	pi.append(a[1])
#print(ai,pi)

price=0
j=0
#for j in range(n):
while j < n:
	# price+=p[j]*a[j]
	# if p[j+1]>p[j]:
	# 	price+=a[j+1]*p[j]
	for k in range(j,n):
		if pi[k]>=pi[j]:
			price+=pi[j]*ai[k]
			if k==n-1:
				j=n-1
				break
		else:
			break
	if j ==n-1 :
		break		
	j=k		

print(price)

