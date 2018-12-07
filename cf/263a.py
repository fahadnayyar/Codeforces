a=list(input().split())
b=list(input().split())
c=list(input().split())
d=list(input().split())
e=list(input().split())
if '1' in a:
	one=a.index('1')
	if one==0 or one ==4:
		print('4')
	elif one ==1 or one == 3:
		print('3')
	else:
		print('2')
elif '1' in b:
	one=b.index('1')
	if one==0 or one ==4:
		print('3')
	elif one ==1 or one == 3:
		print('2')
	else:
		print('1')
elif '1' in c:
	one=c.index('1')
	if one==0 or one ==4:
		print('2')
	elif one ==1 or one == 3:
		print('1')
	else:
		print('0')
elif '1' in d:
	one=d.index('1')
	if one==0 or one ==4:
		print('3')
	elif one ==1 or one == 3:
		print('2')
	else:
		print('1')						
elif '1' in e:
	one=e.index('1')
	if one==0 or one ==4:
		print('4')
	elif one ==1 or one == 3:
		print('3')
	else:
		print('2')						
