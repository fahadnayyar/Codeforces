n=int(input())
a=list(map(int,input().split()))
yo=max(a)
count=0
for i in a :
	count+=(yo-i)
print(count)	