n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))



for i in a:
	if i not in b or a.count(i)!=b.count(i) :
		print(i)
		break
for j in b:
	#print(j)
	if j not in c or c.count(j)!=b.count(j):
		print(j)
		break