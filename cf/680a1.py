t=list(map(int,input().split()))
sumt=sum(t)
arr=[]
#darr=[]
for i in range(0,5):
	for j in range(i,5):
		if i!=j:
			#print(i,j)
			if t[i]==t[j]:
				arr.append(sumt-t[i]-t[j])
				#darr.append(t[i])
for i in range(0,5):
	for j in range(i,5):
		for k in range(j,5):
			if i!=j!=k:
				#print(i,j,k)
				if t[i]==t[j]==t[k]:
					arr.append(sumt-t[i]-t[j]-t[k])				
					#darr.append(t[i])
#print(darr)
#print(arr)
if arr==[]:
	print(sumt)
else:	
	print(min(arr))					