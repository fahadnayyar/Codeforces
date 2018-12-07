k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
arr=[]
array=[]
for p in range(1,d+1):
	array.append(p)
for q in array:
	if q%k==0 or q%l==0	or q%m==0 or q%n==0 :
		arr.append(q)
se=set(arr)
print(len(se))		
