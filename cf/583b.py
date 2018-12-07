n=int(input())
x=list(map(int,input().split()))
i=j=number=count=flag=0
tick=[]
for i in range(n):
	tick.append(0)
flag=0 #flag=0: right, flag=1: left
while sum(tick)!=n:
	if flag==0 and tick[i]==0 and x[i]>number:
		i+=1
	elif flag==1 and ti	

		