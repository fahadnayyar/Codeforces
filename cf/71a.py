a=int(input())
for b in range(a):
	c=input()
	if len(c)>10:
		
		c=c[0]+str(len(c)-2)+c[len(c)-1]
		print(c)
	else:
		print(c)
		