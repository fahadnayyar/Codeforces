n=int(input())
a=list(map(int,input().split()))
maxa=a[0]
mini=a[0]
maxapo=0
minipo=0

for i in range(n):
	if a[i]>maxa:
		maxa=a[i]
		maxapo=i
	if a[i]<mini:
		mini=a[i]
		minipo=i	
ans=abs(minipo-maxapo)
yo=min(minipo,maxapo)+1
ro=max(minipo,maxapo)+1

roro=n-ro+1

if roro>yo:
	ans=ans+roro-1
else:
	ans=ans+yo-1
print(ans)		
