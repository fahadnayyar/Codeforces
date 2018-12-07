a=int(input())
b=input()
count=0
i=0
while True:
	yo=b.find('01',i)
	if yo==-1:
		break
	i=yo+1

j=0
while True:
	yo=b.find('10',j)
	if yo==-1:
		break
	i=yo+1	
	
