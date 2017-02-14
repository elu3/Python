from math import *
from string import *

N = 8
	
def czyBezpiecznie(x,y,rozw):
	global N
	if ((x>=0)and(x<N)and(y>=0)and(y<N)and(rozw[x][y]==-1)):
		return True
	return False


def drukuj_rozw(rozw):
	global N
	for x in range(0,N):
		linijka = ""
		for y in range(0,N):
			znak=" "
			if(rozw[x][y]<10):
				znak = "  "
			linijka = linijka + znak + str(rozw[x][y]) + " "
		print(linijka)
	return 0
 
 
def rozwiazKonika():
	global N
	
	rozw = [[-1 for x in range(N)] for y in range(N)]
	ruchX = [  2, 1, -1, -2, -2, -1,  1,  2 ]
	ruchY = [  1, 2,  2,  1, -1, -2, -2, -1 ]
	
	initx = 0
	inity = 0
	rozw[initx][inity]  = 0;
	if(rozwiazKonia(initx, inity, 1,rozw, ruchX, ruchY) == False):
		print("rozwiazanie nie istnieje")
		return False
	else:
		drukuj_rozw(rozw)
	return 0
 

def rozwiazKonia(x,y,i,rozw, ruchX,ruchY):
	global N
	k=0
	nastepnyX = 0
	nastepnyY = 0
	if(i == N*N):
		return True
	for k in range(0,8):
		nastepnyX = x + ruchX[k]
		nastepnyY = y + ruchY[k]
		if(czyBezpiecznie(nastepnyX,nastepnyY,rozw)):
			rozw[nastepnyX][nastepnyY] = i
			if(rozwiazKonia(nastepnyX,nastepnyY,i+1,rozw,ruchX,ruchY)):
				return True
			else:
				rozw[nastepnyX][nastepnyY] = -1
	return False	

print("rozwiaznie kolejnych ruchow konika metoda baktrace to")
rozwiazKonika()
