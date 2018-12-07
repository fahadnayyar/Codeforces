a=list(map(int,input().split()))
b=list(map(int,input().split()))
yo=0

for i in range(len(b)):
	if b[i]==0:
	
		yo +=1
		
flag=0
for c in range (len(b)):
	if yo!=len(b):
		if b[a[1]-1]!=0:
			if b[c]>=b[a[1]-1]:
				flag+=1
			else:
				continue
		else:
			if b[c]>b[a[1]-1]:
				flag+=1
			else:
				continue		
	 
	else:
		break		
print(flag)			
