n=int(input())
a=list(map(str,input().split()))
s=''
count=0
for i in a:
	s+=i
	if i=='1':
		count+=1

# while i < n-1:

# 	for j in range(i,n-1):
# 		if a[i+1]=0:
if '0' not in s:
	print(count-1)
else:
	j=1	
	while True:
		yo=s.find('0'*j)
		if yo==-1:
			break
		j+=1
	print(count+j-1)	

			
