t=list(map(int,input().split()))
n=t[0]
m=t[1]
a=t[2]
b=t[3]

if m*a>b:
	yo=n//m
	rem=n-(yo*m)
	price1=(yo*b)+(rem*a)
	price2=(yo+1)*b
	print(min(price1,price2))
else:
	price=n*a
	print(price)		