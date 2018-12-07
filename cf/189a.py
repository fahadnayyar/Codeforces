p=list(map(int,input().split()))
q=p[1:]
n=p[0]
a=q[0]
b=q[1]
c=q[2]

x=n//a
n1=n-x
y=n1//b
n2=n1-y
z=n2//c

print(x+y+z)