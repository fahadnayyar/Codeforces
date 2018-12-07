from math import *
def bc(n):
	yo=int(sqrt(n))
	if yo*yo==n:
		return True
	else:
		return False	
def isfibo(n):
	if bc(5*n*n+4) or bc(5*n*n-4):
		return True
	else :
		return False	
n=int(input())
s=""
for i in range(1,n+1):
	if isfibo(i):
		s+="O"
	else:
		s+="o"	
print(s)		