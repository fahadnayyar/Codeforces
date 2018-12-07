a=list(map(str,input().split()))
count=0
for i in range(len(a)):
	if a.count(a[i])==2:
		count+=1
if count==2:
	print(1)
if count==4:
	print(2)	 		

if a[0]!=a[1]!=a[0]!=a[2]!=a[0]!=a[3]!=a[1]!=a[2]!=a[1]!=a[3]!=a[2]!=a[3]:
	print(0)
if a.count(a[0])==3 or a.count(a[1])==3 or a.count(a[2])==3 or a.count(a[3])==3 :
	print(2)

if a[0]==a[1]==a[2]==a[3]:
	print(3)
	