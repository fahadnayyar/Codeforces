a=list(map(int,input().split()))
n=a[0]
t=a[1]
b=list(map(int,input().split()))
b.insert(0,'')
curr=1
while curr<t:
	#print(curr)
	ai=b[curr]
	#print(ai)
	curr=curr+ai
if curr==t:
	print('YES')
else:
	print('NO')		