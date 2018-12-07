a=int(input())
b=input()
flag=0
for c in range(len(b)-1):
	if b[c]==b[c+1]:
		
		flag+=1
print(flag)		
