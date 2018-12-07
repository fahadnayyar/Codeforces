t=int(input())
for i in range(t):
	yo=list(map(int,input().split()))
	n=yo[0]
	k=yo[1]
	kk=list(map(int,input().split()))
	curr=0
	prev=0
	val=[]
	for j in range(k):
		curr=i
		diff=curr-prev
		if diff%2==0:
			bhagg=diff//2
		else:
			bhagg=((diff//2))+1
		prev=i	
		val.append(bhagg)
	diff=n-curr
	if diff%2==0:
		bhagg=diff//2
	else:
		bhagg=(diff//2)+1
		#prev=i	
		val.append(bhagg)		
	print(min(val))	