s=input()
n=len(s)
count=0
for i in range(n):
	if s[i]=="o":
		count+=1
yo=n-count
if count==0:
	print("YES")
elif (yo%count==0):
	print("YES")
else:
	print("NO")			