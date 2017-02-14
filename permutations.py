def perm(s,i,n):
	if(i==n):
		print(s)
	else:
		for j in range(i,n+1):
			s[i],s[j] = s[j],s[i]
			perm(s,i+1,n)
			s[i],s[j] = s[j],s[i]
	return 0
	
N=int(input('Put the number of set: '))
s=[0]*(N)
print("Permutations: ")
for i in range(0,N):
   s[i] = i+1
perm(s, 0, N-1)
