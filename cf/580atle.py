a=int(input())
b=list(map(int,input().split()))
finallist=[]
#for i in range():
if a==1:
	print(1)

else:

	t=0

	while t<a-1:
		currlist=[b[t]]
		i=t
		while i<a-1:
			#if i==a-1:
				#break
			if b[i+1]>=b[i]:
				currlist.append(b[i+1])
				#print(currlist)
				i+=1
				#print(i)
			#elif 	
			else:
				break
			#if len(currlist)==a	

		finallist.append(currlist)
		#print(finallist)
		t=i+1
	ans=len(finallist[0])
	for p in finallist:
		if len(p)>ans:
			ans=len(p)
	print(ans)						