a=list(map(int,input().split()))
yo=min(a[0],a[2],a[3])
a[0]=a[0]-yo
ro=min(a[0],a[1])
print((256*yo)+(32*ro))