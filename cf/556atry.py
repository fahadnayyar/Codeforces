a=int(input())
b=input()
i=0
while True:
	if b[i]!=b[i+1]:
		#b.remove(b[i])
		#b.remove(b[i+1])
		b=b[:i]+b[i+2:]
		print(b)
		i=0
	else:
		i+=1
	if len(b)==0:
		break
print(len(b))			
