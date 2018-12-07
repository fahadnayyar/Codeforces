n=int(input())
if n==1:
	b=int(input())
	print(0)
else:	
	arr=list(map(int,input().split()))
	a=arr[0]
	b=arr[1]
	d=b-a
	ansar=[]



	flag1=0
	ans1=0  # a,b
	a1=a
	d1=d
	for i in range(2,n):
		if abs(arr[i]-(a1+(i)*d1))==1:
			ans1+=1
		elif abs(arr[i]-(a1+(i)*d1))==0:
			continue
		else:
			flag1=1
			break
	if flag1==0:
		ansar.append(ans1)

	flag2=0
	ans2=1  # a,b-1
	a2=a
	d2=d-1
	for i in range(2,n):
		if abs(arr[i]-(a2+(i)*d2))==1:
			ans2+=1
		elif abs(arr[i]-(a2+(i)*d2))==0:
			continue	
		else:
			flag2=1
			break
	if flag2==0:
		ansar.append(ans2)

	flag3=0
	ans3=1 # a-1,b
	a3=a-1
	d3=d+1
	for i in range(2,n):
		# print(a3+(i)*d3)
		# print(ans3)
		if abs(arr[i]-(a3+(i)*d3))==1:
			ans3+=1
		elif abs(arr[i]-(a3+(i)*d3))==0:
			continue	
		else:
			flag3=1
			break
	if flag3==0:
		ansar.append(ans3)

	flag4=0
	ans4=1	# a+1,b
	a4=a+1
	d4=d-1
	for i in range(2,n):
		
		if abs(arr[i]-(a4+(i)*d4))==1:
			ans4+=1
		elif abs(arr[i]-(a4+(i)*d4))==0:
			continue	
		else:
			flag4=1
			break
	if flag4==0:
		ansar.append(ans4)

	flag5=0
	ans5=1	# a,b+1
	a5=a
	d5=d+1
	for i in range(2,n):
		if abs(arr[i]-(a5+(i)*d5))==1:
			ans5+=1
		elif abs(arr[i]-(a5+(i)*d5))==0:
			continue	
		else:
			flag5=1
			break
	if flag5==0:
		ansar.append(ans5)

	flag6=0
	ans6=2	# a+1,b+1
	a6=a+1
	d6=d
	for i in range(2,n):
		if abs(arr[i]-(a6+(i)*d6))==1:
			ans6+=1
		elif abs(arr[i]-(a6+(i)*d6))==0:
			continue	
		else:
			flag6=1
			break
	if flag6==0:
		ansar.append(ans6)

	flag7=0
	ans7=2	# a-1,b-1
	a7=a-1
	d7=d
	for i in range(2,n):
		if abs(arr[i]-(a7+(i)*d7))==1:
			ans7+=1
		elif abs(arr[i]-(a7+(i)*d7))==0:
			continue	
		else:
			flag7=1
			break
	if flag7==0:
		ansar.append(ans7)

	flag8=0
	ans8=2  # a+1,b-1
	a8=a+1
	d8=d-2
	for i in range(2,n):
		if abs(arr[i]-(a8+(i)*d8))==1:
			ans8+=1
		elif abs(arr[i]-(a8+(i)*d8))==0:
			continue	
		else:
			flag8=1
			break
	if flag8==0:
		ansar.append(ans8)

	flag9=0
	ans9=2  # a-1,b+1
	a9=a-1
	d9=d+2
	for i in range(2,n):
		if abs(arr[i]-(a9+(i)*d9))==1:
			ans9+=1
		elif abs(arr[i]-(a9+(i)*d9))==0:
			continue	
		else:
			flag9=1
			break
	if flag9==0:
		ansar.append(ans9)
	#print(ansar)
	if ansar==[]:
		print(-1)
	else:	
		print(min(ansar))	