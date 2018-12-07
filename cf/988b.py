class st:
	def __init__(self,s,n):
		self.s=s
		self.n=n
arr=[]
n=int(input())
for i in range(n):
	s=input()
	arr.append(st(s,len(s)))
arr.sort(key = lambda st:st.n )
flag=0
for i in range(n-1):
	if arr[i+1].s.find(arr[i].s)==-1:
		flag=1
		break
if flag==1	:
	print("NO")
else:
	print("YES")
	for i in arr:
		print(i.s)		 	