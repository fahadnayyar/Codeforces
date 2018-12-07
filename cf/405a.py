a=int(input())
b=list(map(int,input().split()))
b.sort()
b=str(b)
b=b.replace(',','')

print(b[1:-1])