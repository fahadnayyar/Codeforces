a=list((input()))
for i in range(len(a)):
	if 9-int(a[i])<int(a[i]):
		a[i]=str(9-int(a[i]))
if a[0]=='0':
	a[0]=str(9)
s=''
for i in a:
	s+=i

print(int(s))			
