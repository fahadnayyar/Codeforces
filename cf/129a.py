n=int(input())
x=list(map(int,input().split()))
odd=0
even=0
for i in x:
	if i%2==0:
		even+=1
	else:
		odd+=1
if odd%2==0:
	print(even)
else:
	print(odd)				