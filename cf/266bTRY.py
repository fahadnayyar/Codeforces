a=list(map(int,input().split()))
b=input()
t=0
for j in range(a[1]):
	if a[0]%2==0:
		for i in range(0,(len(b)-1),2):
			if b[i]!=b[i+1]:
				b=b[:i]+'GB'+b[i+2:]
	else:
		for i in range(0,(len(b)-2),2):
			if b[i]!=b[i+1]:
				b=b[:i]+'GB'+b[i+2:]			
print(b)