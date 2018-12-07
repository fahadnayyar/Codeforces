yoar=list(map(int,input().split()))
n=yoar[0]
w=yoar[1]
arr=list(map(int,input().split()))
sumar=[]
sumar.append(arr[0])
for i in range(1,n):
	sumar.append(arr[i]+sumar[i-1])
mini=min(sumar)	
maxa=max(sumar)

lf=0
rg=0
if maxa>w:
	print(0)
else:
	if mini<0:
		lf=-mini
	else:
		lf=0
	if maxa<=0:
		rg=w
	else:
		rg=w-maxa
	if lf>rg:
		print(0)
	else:
		print(rg-lf+1)					



# if maxa<0 and mini <0:
# 	if abs(mini)>=w:
# 		print(0)
# 	else:
# 		print(w-abs(mini)+1)	


# elif maxa>=0 and  mini<=0:

# 	if maxa>=w or abs(mini)>=w:
# 		print(0)
# 	else:
# 		print(w-maxa-abs(mini)+1)	
# else:
# 	if (maxa>=w):
# 		print(0)
# 	else:
# 		print(w-maxa+1)		