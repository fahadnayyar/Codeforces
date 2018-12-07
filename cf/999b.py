def giveDiv(n):
	retar=[]
	for i in range(1,n//2+2):
		if n%i==0:
			retar.append(i)
	if retar[-1]!=n:
		retar.append(n)
	return retar

n=int(input())
divar=giveDiv(n)
#print(divar)
s=input()
for i in divar:
	retain=s[i:]
	reverse=s[:i]
	reverse=reverse[::-1]	
	s=reverse+retain
print(s)			