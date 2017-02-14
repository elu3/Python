def subset(n,k):
    if k==0:
        yield set()
    elif k==n:
        yield set(range(1,n+1))
    else:
        for i in subset(n-1,k):
            yield i
        for i in subset(n-1,k-1):
            yield i|{n}
a=int(input('Put the number of set elements: '))
b=int(input('Put the number of subset elements: '))
for i in subset(a,b):
    print(i)
