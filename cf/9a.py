def printans(to):
	if to==1:
		print("1/1")
	elif to==2:
		print("5/6")
	elif to==3:
		print("2/3")		
	elif to==4:
		print("1/2")	
	elif to==5:
		print("1/3")
	elif to==6:
		print("1/6")
			
yo=list(map(int,input().split()))
ro=max(yo);

printans(ro)

