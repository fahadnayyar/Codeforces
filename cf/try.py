a=list(map(int,input().split()))
n=''
for b in range(1,a[0]+1):
	n+=str(b)
#print(n)
even=''
odd=''
for c in range(len(n)):
	if int(n[c])%2==0:
		even+=n[c]
	else:
		odd+=n[c]
if '0' in even:
	even.remove('0')
if '1' in even:
	even.remove('1')
#print(even)		

final=odd + even
#print(final)
print(int(final[a[1]-1]))


