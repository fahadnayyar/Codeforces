a=list(map(int,input().split()))
n=a[0]
x=a[1]
count=0
for i in range(1,n+1):
	# if x%n and n**2!=x:
	# 	count+=2
	# elif x%n and n**2==x:
	# 	count+=1
	#print(x,i)
	if x%i==0:


		if x<=i*n:
			count+=1

		# for j in range(1,n+1):
		# 	if i*j==x :
		# 		#print(i,j)
		# 		count+=1

print(count)			