n=int(input())
a=list(map(int,input().split()))

#count=0
for i in a:
	count=0
	for j in  range(2,(i//2)+1):
		if i%j==0:
			count+=1
		if count>1:
			print('NO')
			break	
	if count==1:
		print('YES')
	elif count<1:
		print('NO')			