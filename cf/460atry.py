a=list(map(int,input().split()))
n=a[0]
m=a[1]
k=0
while True:
	b=n-m+1
	if b>0:
		k+=1
		if b>m:
			
			n=b
			continue
		elif b==m:
			k+=1
			b=1d
			break
		else:
			break		
	elif b==0:
		k+=1
		b=0
		break

	else:
		#k+=1
		b=n
		break	
r=(m*k)+b
print(r)