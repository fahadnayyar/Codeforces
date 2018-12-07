mat=list(map(int,input().split()))
n=mat[0]
colour=0
for i in range(n):
	a=list(map(str,input().split()))
	if 'C' in a or 'M' in a or 'Y' in a :
		colour=1

if colour==1:
	print('#Color')
elif colour==0:
	print('#Black&White')			

