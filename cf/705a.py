n=int(input())
s=''
for i in range(1,n+1):
	if i%2==1:
		s+='I hate that '
	else:
		s+='I love that '
s=s[:-5]+'it'

print(s)			
