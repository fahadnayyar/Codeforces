a=list(map(int,input().split()))
x1=a[0]
y1=a[1]
x2=a[2]
y2=a[3]

if x1!=x2 and y1!=y2 and abs(x1-x2)!=abs(y1-y2):
	print(-1)
else:
	if x1==x2:
		side=abs(y1-y2)
		print(x1+side,y1,x2+side,y2)
	elif y1==y2:
		side=abs(x1-x2)
		print(x1,y1+side,x2,y2+side)
	else:
		print(x1,y2,x2,y1)
				