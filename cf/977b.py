n=int(input())
s=input()
sarr=[]
intarr=[]
for i in range(n-1):
	ss=s[i:i+2]
	if ss not in sarr:
		sarr.append(ss)
		intarr.append(1)
	else:
		yo=sarr.index(ss)
		intarr[yo]+=1
mini=0
minind=0

l=len(intarr)
for i in range(l):
	if intarr[i]>mini:
		mini=intarr[i]
		minind=i
print(sarr[minind])		
