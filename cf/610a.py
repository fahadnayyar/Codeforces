n=int(input())
if n%2!=0:
	print(0)
else:
	yo=n//2
	if yo%2==0:
		print((yo//2)-1)
	else:
		print(yo//2)		
