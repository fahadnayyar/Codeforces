from copy import *
n=int(input())
arr=list(map(int,input().split()))
arr1=deepcopy(arr)
for i in arr:
	count=arr1.count(i)
	j=0
	while (count!=1):
		arr1.remove(i)
		count=count-1
print(len(arr1))
for i in arr1:
	print(i,end=" ")
print()			