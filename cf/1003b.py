yoar=list(map(int,input().split()))
a=yoar[0]
b=yoar[1]
x=yoar[2]
x1=x
# if (x%2==0):
# 	y=x//2
# 	left1=a-y
# 	left0=b-y
# 	print("1"*left1+"01"*y+"0"*left0)
# else:	
# 	y=x//2
# 	y1=y+1
# 	y0=y
# 	left1=a-y1
# 	left0=a-y0
# 	print("1"*left1+"10"*y+"1"+"0"*left0)

st= "1"
a1=a #0
b1=b-1 #1
for i in range(a+b-1):
	if x>1:
		if st[-1]=="1":
			st=st+"0"
			a1-=1
		else:
			st=st+"1"	
			b1-=1
		x-=1	

	else:
		if st[-1]=="0" and a1>0:
			st=st+"0"
			a1-=1
		elif st[-1]=="1" and b1>0:
			st=st+"1"
			b1-=1
		elif a1>0:
			st=st+"0"
			a1-=1
		else:
			st=st+"1"					
			b1-=1
count=0
for i in range(1,a+b):
	if (st[i]!=st[i-1])	:		
		count+=1
if (count==x1):
	print(st)
else:
	print(st[-1]+st[:-1])			