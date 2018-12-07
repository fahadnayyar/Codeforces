n=int(input())
count=0
previnp=[]
for i in range(n):
	x=input()
	previnp.append(x)
	if x[:2]!='OO' and x[3:]!='OO':
		count+=1
		#print(count,x)
	#else:
		#print(count,'yo',x)	
if count==n:
	print ('NO')	

else: 

	print('YES')
	toto=0
	for i in range(n):
		x=previnp[i]
		if toto==1:
			print(x)
		else:	

			if x[:2]=='OO' :
				print('++|'+x[3:])
				toto=1
			elif x[3:]=='OO' :
				print(x[:2]+'|++')
				toto=1
			else:
				print(x)		
