def prime_exp(n,p):
	count=0
	while n%p ==0:
		count+=1
		n=n/p
	return count	
def shade32off(n):
	two=prime_exp(n,2)
	three=prime_exp(n,3)
	#print(two)
	#print(three)
	ans=n//2**two
	ans=ans//3**three
	return ans

#print(prime_exp(75,3))

n=int(input())
arr=list(map(int,input().split()))
prev=shade32off(arr[0])
#print(prev)
#print()
flag=0
for i in arr:
	yo=shade32off(i)
	#print(yo)
	if yo!=prev:
		flag=1
		print("No")
		break
if flag==0:
	print("Yes")		
	
