n=int(input())
l=len(str(n))
#l=l-1
#yo=l-1
#ro=(10**(l-1)-1)
ro=int(((9*l-10)*(10**(l-1))+1)/9)
#print(int(ro))

if l!=1:
	yo=n-int('9'*(l-1))
else:
	yo=n
#print(yo)
yoyo=yo*l
ans=ro+yoyo
print(ans)