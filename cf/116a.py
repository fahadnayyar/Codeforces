a=int(input())
flag=0
d=[]
for b in range(a):
	c=list(map(int,input().split()))
	flag=flag-c[0]+c[1]
	d.insert(0,flag)	
d.sort()
print(max(d))	

