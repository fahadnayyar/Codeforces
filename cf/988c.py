class elem:
	def __init__(self,val,ind,seq):
		self.val=val
		self.ind=ind
		self.seq=seq
k=int(input())
elemar=[]
for w in range(k):
	n=int(input())
	arr=list(map(int,input().split()))
	suma=sum(arr)
	for i in range(n):
		arr[i]=suma-arr[i]
	for i in range(n):
		elemar.append(elem(arr[i],i+1,w+1))

elemar.sort(key= lambda elem: elem.val)

# for i in elemar:
# 	print(i.val,end=" ")
# print()	
# for i in elemar:
# 	print(i.seq,end=" ")
# print()	
l=len(elemar)
flag=0
for i in range(1,l):
	#print(elemar[i-1].val,elemar[i-1].seq,elemar[i-1].ind,elemar[i].val,elemar[i].seq,elemar[i].ind)
	if elemar[i].val==elemar[i-1].val and elemar[i].seq!=elemar[i-1].seq:
		flag=1
		print("YES")
		print(elemar[i].seq,elemar[i].ind)
		print(elemar[i-1].seq,elemar[i-1].ind)
		break
if flag==0:
	print("NO")		
1073741824	