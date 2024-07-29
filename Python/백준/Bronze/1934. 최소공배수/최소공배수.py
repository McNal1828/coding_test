def getGcd(x,y):
    while y:
        x,y = y,x%y
    return x

def getLcm(x,y):
    gcd = getGcd(x,y)
    return x * y // gcd

score_list = []
count = int(input())

for i in range(count):
    a,b = map(int,input().split(' '))
    score_list.append(getLcm(a,b))

for score in score_list:
    print(score)