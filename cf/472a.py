from math import sqrt
from math import ceil
def isprime(n):
	if n==2:
		return True

	for i in range(2,ceil(sqrt(n))+1):
		if n%i==0:
			return False
	return True		




a=int(input())

for i in range(1,a+1):
	j=a-i
	if not(isprime(i) or isprime(j)):
		print(i,j)
		break
			
