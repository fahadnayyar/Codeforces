n=int(input())
yo=n//7
ro = n%7



if ro == 1:
	print(yo*2,(yo*2)+1)
elif ro==0:
	print(yo*2,yo*2)
elif ro==6:
	print((yo*2)+1,(yo*2)+2)
else:
	print(yo*2,(yo*2)+2)