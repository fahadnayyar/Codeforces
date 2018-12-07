a=list(map(int,input().split()))
n=a[0]
h=a[1]
b=list(map(int,input().split()))
flag=0
for i in b:
	if i>h:
		flag+=2
	else:
		flag+=1
print(flag)			