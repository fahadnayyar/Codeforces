a=list(map(int,input().split()))
n=a[0]
t=a[1]
s=str(input())
p=s
for i in range(t):	
	s=p
	b=0
	
	p=''
	
	while b<=n-2 :
		if s[b]=='B':
			if b==n-2:
				if s[n-1]=='B':
					p+='BB'
					#print(p)	
			elif s[b+1]=='G':
				p+='GB'
				b+=1
				#print(p)
			else:
				p+=s[b]
				#print(p)

			
		else:
			p=p+s[b]
			#print(p)
			if b==n-2:
				#p+=s[n-2]
				p+=s[n-1]
				#print(p)
		b+=1

print(p)				

