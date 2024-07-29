def gotThree(x):
    return 10000+x*1000

def gotTwo(x):
    return 1000+x*100

def gotOne(x):
    return x*100


inputlist = list(map(int,input().split()))
inputlist.sort(reverse=True)
[a,b,c] = inputlist
if(a==b):
    if(a==c):
        print(gotThree(a))
    else:
        print(gotTwo(a))
else:
    if(b==c):
        print(gotTwo(b))
    else:
        print(gotOne(a))