from math import log
t=int(input())
for i in range(t):
	n=int(input())
	yo=int(log(n,2))
	#print(yo)
	ans=int(((n*(n+1))/2)) - int((2*(2**(yo+1)-1)))
	print(int(n*(n+1)/2),int(2*(2**(yo+1)-1)))
	print(int(ans))
	
