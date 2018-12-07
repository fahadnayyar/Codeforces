from math import sqrt
yoar = list(map(int,input().split()))
n = yoar[0]
k = yoar[1]
divar=[]
divar1=[]
yo = sqrt(n)
flag = 0
if yo*yo==n:
	yo=int(yo)
	flag=1
else:
	yo=int(yo)+1	

for i in range(1,yo):
	if (n%i==0):
		divar.append(i)
		divar1.append(n//i)
if flag==1:
	divar.append(yo)		
l1=len(divar1)
for i in range(l1-1,-1,-1):
	divar.append(divar1[i])

#divar=list(set(divar))
#print(divar)
if len(divar)<k:
	print(-1)
else:		
	print(divar[k-1])