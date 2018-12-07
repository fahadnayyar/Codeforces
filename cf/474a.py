a=input()
b=input()
c='qwertyuiopasdfghjkl;zxcvbnm,./'
#d='asdfghjkl;'
#e='zxcvbnm,./'
if a=='R':
	ans=''
	for i in range(len(b)):
		p=c.find(b[i])
		ans+=c[p-1]
if a=='L':
	ans=''
	for i in range(len(b)):
		p=c.find(b[i])
		ans+=c[p+1]
print(ans)				
