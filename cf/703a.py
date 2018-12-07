n=int(input())
mis=0
chris=0

for i in range(n):
	a=list(map(int,input().split()))
	if a[0]>a[1]:
		mis+=1
	if a[0]<a[1]:
		chris+=1

if mis>chris:
	print('Mishka')
elif chris>mis:
	print('Chris')
else:
	print('Friendship is magic!^^')					