a=list(map(int,input().split()))
d1=a[0]
d2=a[1]
d3=a[2]


ans=min(d1+d2+d3,2*(d1+d2),2*(d2+d3),2*(d3+d1))
print(ans)


# if d1+d2+d3 < 2*(d1+d2):
# 	print(d1+d2+d3)
# else:
# 	print(2*(d1+d2))	