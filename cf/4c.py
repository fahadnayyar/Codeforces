n=int(input())
database=[]
for i in range(n):
	a=input()
	if a not in database:
		print('OK')
		database.append(a)
	else:
		count=0
		for j in database:
			if j[:len(a)] == a:
				count+=1
		yo=a+str(count)
		print(yo)
		database.append(yo)

					
