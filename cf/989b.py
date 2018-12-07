yoar=list(map(int,input().split()))
n=yoar[0]
p=yoar[1]
s=list(input())
flag=0
for i in range(n-p):
	#print(i)
	if s[i]==s[i+p]!=".":
		flag+=1
		continue
	elif s[i]==s[i+p]==".":	
		s[i]="0"
		s[i+p]="1"
	elif s[i]=="1":
		if s[i+p]=="0":
			continue
			#flag=1
			#break
		elif s[i+p]==".":
			s[i+p]="0"
	elif s[i+p]=="1":
		if s[i]=="0":
			continue
			# flag=1
			# break
		elif s[i]==".":
			s[i]="0"				
	elif s[i]=="0":
		if s[i+p]=="1":
			continue
			#flag=1
			#break
		elif s[i+p]==".":
			s[i+p]="1"
	elif s[i+p]=="0":
		if s[i]=="1":
			continue
			# flag=1
			# break
		elif s[i]==".":
			s[i]="1"

if flag==n-p:
	print("No")
else:
	#print(s)
	for i in range(n):
		if s[i]==".":
			s[i]="0"


	for i in s:
		print(i,end="")
	print()							