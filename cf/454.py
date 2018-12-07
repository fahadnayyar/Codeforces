n=int(input())
for i in range(1,n+1):
	if i>(n//2)+1:
		yo=i-(n//2)+1
		i=(n//2)+1-yo


	print('*'*(n//2),end='')
	print(str('D'*((2*i)-1)),end='')
	#print(('*'*(i//2))+('D'*((2*i)-1))+('*'(i//2)),end='')
	print('*'*(n//2))