a=int(input())
if a>0:
	print(a)

else:
	
	
	yo=str(a)
	p=int(yo[-1])
	q=int(yo[-2])
	if p>q:
		ans=yo[:-1]
		print(int(ans))
	else:
		ans=yo[:-2]+yo[-1]
		print(int(ans))	

