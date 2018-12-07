yoar=list(map(int,input().split()))
n=yoar[0]
b=yoar[1]
arr=list(map(int,input().split()))
cutar=[]
odar=[]
if (arr[0]%2==0):
	odar.append(0)
else:
	odar.append(1)


for i in range(1,n):
	if (arr[i]%2==0):
		odar.append(odar[i-1])
	else:
		odar.append(odar[i-1]+1)

for i in range(1,n):
	odd = odar[i-1]
	even = i-odd
	if even==odd:
		cutar.append(abs(arr[i]-arr[i-1]))
cutar.sort()
ans=0
cur=0
for i in cutar:
	if cur+i>=b:
		break
	ans+=1
	cur=cur+i
print(ans)		
