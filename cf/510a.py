a=list(map(int,input().split()))
n=a[0]
m=a[1]

for i in range(1,n+1):
	if i%4==1 :
		print('#'*m)
	elif i%4==3:
		print('#'*m)	
		
	elif i%4==2:
		print('.'*(m-1)+'#')
	elif i%4==0:
		print('#'+'.'*(m-1))	
			
