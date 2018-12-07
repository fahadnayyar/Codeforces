r=list(map(int,input().split()))
n=r[0]
d=r[1]
t=list(map(int,input().split()))
suma=0
for i in t:
	suma+=i+10
suma=suma-10
rem=d-suma
jokes=((n-1)*2)+(rem//5)

if rem <0:
	print(-1)
else:
	print(jokes)		