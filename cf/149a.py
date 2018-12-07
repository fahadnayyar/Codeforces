a=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
b.insert(0,0)
#print(b)
sum=0
i=1
while sum<a:
	#print(i)
	sum+=b[i]
	#i+=1
	if i==12 and sum<a:
		break
	i+=1
# if sum==a:
# 	print(i)
# else:
# 	print(i+1)		
if i==12 and sum<a:
	print(-1)
else:
	print(i-1)
