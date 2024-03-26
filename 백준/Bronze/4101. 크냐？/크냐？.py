res = []
while True:
    A,B=map(int,input().split())
    if(A==0 and B==0):
        break
    if(A>B):
        res.append('Yes')
    else:
        res.append('No')
for r in res:
    print(r)