from math import *
a=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
t=0
for p in range(a):
	t+=b[p]

flag=0
count=0
for c in range(a):
	flag+=b[c]
	count+=1
	if flag > floor(t/2):
		break
	else:
		continue
print(count)			
