a=input()
cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small='abcdefghijklmnopqrstuvwxyz'
#print(len(cap),len(small))
countcap=0
countsmall=0
for i in a:
	if i in cap:
		countcap+=1
	else:
		countsmall+=1

if countcap>countsmall:
	print(a.upper())
else:
	print(a.lower())				