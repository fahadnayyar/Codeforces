yo=list(map(int,input().split()))
n=yo[0]
k=yo[1]
a=list(map(int,input().split()))
t=list(map(int,input().split()))
arr=[]
for i in range(n):
	arr.append(0)	
for i in range(n):
	if t[i]==0 :
		arr[i]=a[i]
	else:
		arr[i]=0
i=0
j=k-1
indi=0
indj=k-1
mini=sum(arr[i:j+1])
while (j!=n-1):
	if mini-arr[i]+arr[j+1]>mini:
		mini=mini-arr[i]+arr[j+1]
		indi=i+1
		indj=j+1
	i+=1
	j+=1	
ans=0
#ansarr=[]
for i in range(n):
	if indi<=i<=indj:
		#print(ans)
		ans+=a[i]
		#print(ans)
		#ansarr.append(ans)
	else:
		if t[i]==1:
			ans+=a[i]
			#ansarr.append(ans)
			#print(ans)
		#else:
			#ansarr.append(0)	
# for j in a:
# 	print(j,end=" ")
# print()	
for j in arr:
	print(j,end=" ")
print()	

# for j in ansarr:
# 	print(j,end=" ")
# print()	


#print(indi,indj)
print(ans)				