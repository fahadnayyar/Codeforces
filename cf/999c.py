# in python list append is O(1) but pop or removing from other indexes is O(n).

yoar=list(map(int,input().split()))
n=yoar[0]
k=yoar[1]
s=input()
dic={}
arr=[]

lar=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in lar:
	dic[i]=[]
for i in range(n):
	arr.append(s[i])
for i in range(n-1,-1,-1):
	#arr.append(s[i])
	# if arr[i] not in dic:
	# 	dic[arr[i]]=[]
	dic[s[i]].append(i)
# for i in dic:
# 	print(dic[i])	
for i in range(k):
	if dic["a"]!=[]:
		ind = dic["a"].pop()
		arr[ind]=-1		
	elif dic["b"]!=[]:
		ind = dic["b"].pop()
		arr[ind]=-1	
	elif dic["c"]!=[]:
		ind = dic["c"].pop()
		arr[ind]=-1	
	elif dic["d"]!=[]:
		ind = dic["d"].pop()
		arr[ind]=-1	
	elif dic["e"]!=[]:
		ind = dic["e"].pop()
		arr[ind]=-1	
	elif dic["f"]!=[]:
		ind = dic["f"].pop()
		arr[ind]=-1	
	elif dic["g"]!=[]:
		ind = dic["g"].pop()
		arr[ind]=-1	
	elif dic["h"]!=[]:
		ind = dic["h"].pop()
		arr[ind]=-1
	elif dic["i"]!=[]:
		ind = dic["i"].pop()
		arr[ind]=-1	
	elif dic["j"]!=[]:
		ind = dic["j"].pop()
		arr[ind]=-1	
	elif dic["k"]!=[]:
		ind = dic["k"].pop()
		arr[ind]=-1	
	elif dic["l"]!=[]:
		ind = dic["l"].pop()
		arr[ind]=-1	
	elif dic["m"]!=[]:
		ind = dic["m"].pop()
		arr[ind]=-1	
	elif dic["n"]!=[]:
		ind = dic["n"].pop()
		arr[ind]=-1	
	elif dic["o"]!=[]:
		ind = dic["o"].pop()
		arr[ind]=-1	
	elif dic["p"]!=[]:
		ind = dic["p"].pop()
		arr[ind]=-1	
	elif dic["q"]!=[]:
		ind = dic["q"].pop()
		arr[ind]=-1	
	elif dic["r"]!=[]:
		ind = dic["r"].pop()
		arr[ind]=-1	
	elif dic["s"]!=[]:
		ind = dic["s"].pop()
		arr[ind]=-1	
	elif dic["t"]!=[]:
		ind = dic["t"].pop()
		arr[ind]=-1	
	elif dic["u"]!=[]:
		ind = dic["u"].pop()
		arr[ind]=-1	
	elif dic["v"]!=[]:
		ind = dic["v"].pop()
		arr[ind]=-1	
	elif dic["w"]!=[]:
		ind = dic["w"].pop()
		arr[ind]=-1	
	elif dic["x"]!=[]:
		ind = dic["x"].pop()
		arr[ind]=-1	
	elif dic["y"]!=[]:
		ind = dic["y"].pop()
		arr[ind]=-1	

	elif dic["z"]!=[]:
		ind = dic["z"].pop()
		arr[ind]=-1	
flag=0
for i in arr:
	if (i!=-1):
		flag=1
		print(i,end="")

if flag==1:
	print()			
																																																					