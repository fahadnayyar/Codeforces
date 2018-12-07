a=int(input())
flag=0
for i in range(a):
	b=list(map(int,input().split()))
	if (b[1]-b[0]) > 1:
		flag+=1

print(flag)		
