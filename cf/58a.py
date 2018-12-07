a=input()
if 'h'in a and  'e'in a and 'l'in a and 'o' in a :
	b=a.count('l')
	if b>1:
		h=a.find('h')
		e=a.find('e',h+1)
		l1=a.find('l',e+1)
		l2=a.find('l',l1+1)
		o=a.find('o',l2+1)
		if h==-1 or e==-1 or l1==-1 or l2==-1 or o==-1 :
			print('NO')

		else:
			print('YES')
	else:
		print('NO')		
else:
	print('NO')				  
