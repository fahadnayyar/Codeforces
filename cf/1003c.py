def givemax(arr,k,ar1,n):
	maxa=0
	for i in range(n-k+1):
		yo=(arr[i+k-1]-arr[i]+ar1[i])
		#print(yo)
		if maxa<yo:
			maxa=yo
	return maxa/k		

yoar=list(map(int,input().split()))
n=yoar[0]
k=yoar[1]
arr=list(map(int,input().split()))
sumar=[]
sumar.append(arr[0])

for i in range(1,n):
	sumar.append(sumar[i-1]+arr[i])
#print(sumar)	
maxans=0
for i in range(k,n+1):
	cur=givemax(sumar,i,arr,n)	
	#print(cur)
	if (maxans<cur):
		maxans=cur
print(maxans)		