def subset(n,k):#n - number of elements, k- number of subsets elements
    if k==0:
        yield set()
    elif k==n:
        yield set(range(1,n+1))
    else:
        for i in subset(n-1,k):#option1
            yield i
        for i in subset(n-1,k-1):
            yield i|{n}#union

def all_subsets(N):
	for p in range(0,N+1):
		for i in subset(N,p):
			print(i)
			
a=int(input('Put the number of set elements: '))
all_subsets(a)
