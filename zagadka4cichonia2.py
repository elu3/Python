from math import *
from string import *



def wstaw(tekst, nowe, pozycja):
	return tekst[:pozycja] + nowe + tekst[pozycja:]

def zamien_jeden_znak(text,indeks_znaku, znak):
	nowy = text[:indeks_znaku] + znak + text[(indeks_znaku+1):]
	return nowy
	

def znajdz_indeks_nastepnego_miejsca_do_wstawienia_nawiasu_w_dol(wyrazenie, indeks_startowy):#M8
	if (indeks_startowy==0):
		return 0
	j = indeks_startowy
	minieto_prawe = 0
	minieto_lewe  = 0
	operator_odwiedzony = 0;
	odwiedzone_wyrazenie_nawias = 0
	while (j>=0):
		if ((wyrazenie[j] == ")")or(wyrazenie[j] == "(")):
			if (wyrazenie[j] == ")"):
				minieto_prawe = minieto_prawe + 1
			if (wyrazenie[j] == "("):
				minieto_lewe  = minieto_lewe + 1
			if((minieto_prawe == minieto_lewe)):
				odwiedzone_wyrazenie_nawias = odwiedzone_wyrazenie_nawias + 1
				operator_odwiedzony = 0
		if ((wyrazenie[j] == "+")or(wyrazenie[j] == "-")or(wyrazenie[j] == "*")):
			operator_odwiedzony = operator_odwiedzony+1
		if (((minieto_prawe==0)and(minieto_lewe==0))and(operator_odwiedzony >= 2)and(odwiedzone_wyrazenie_nawias==0)):
			return j;
		if ((operator_odwiedzony >= 2) and (minieto_prawe == minieto_lewe)and(odwiedzone_wyrazenie_nawias>=1)):
			if(j!=0):
				if((wyrazenie[j-1]!="(")and(wyrazenie[j-1]!=")")):
					return j
		j=j-1
	return 0
	
def zbuduj_formulke(nawiasy, operatory, liczby):#M6
	wyrazenie = ""
	Nliczb = len(liczby)
	Nop = Nliczb-1
	
	wyrazenie ="(" + nawiasy[:]
	i = 0
	while (i<Nliczb):
		if (i == 0):
			wyrazenie = wyrazenie.replace("(",str(liczby[i]),1)
		else:
			wyrazenie = wyrazenie.replace("(",operatory[i-1]+str(liczby[i]),1)
		i = i+1
	
	i = 0	
	while (i<len(wyrazenie)):
		if (wyrazenie[i]==")"):
			j = i - 1
			nastepny_nawias = -1
			minieto_prawe = 0
			minieto_lewe  = 0
			while (j>=0):
				if ((wyrazenie[j] == "+")or(wyrazenie[j] == "-")or(wyrazenie[j] == "*")or(wyrazenie[i]==")")or(wyrazenie[i]=="(")):
					nastepny_nawias = znajdz_indeks_nastepnego_miejsca_do_wstawienia_nawiasu_w_dol(wyrazenie, j)#M7
					if (nastepny_nawias != 0):
						wyrazenie = wstaw(wyrazenie,"(",nastepny_nawias+1)
					else:
						wyrazenie = wstaw(wyrazenie,"(",nastepny_nawias)
					i=i+1
					break
				j = j-1
		i = i+1
	return wyrazenie
	

ilosc_kombinacji = 0
ilosc_rozwiazan = 0
def licz_wyrazenie(y,liczby,operatory,nawiasy,level_op,naw_pozycja,naw_otwarty,naw_zamkniety):
	Nliczb = len(liczby)
	Nop = Nliczb - 1 
	global ilosc_kombinacji
	global ilosc_rozwiazan
	if(level_op==1):
		if (naw_zamkniety==Nop):  # "()(())", "+-*" , [1,2,3,4]
			#M5
			wyrazenie = zbuduj_formulke(nawiasy, operatory, liczby)
			wynik = eval(wyrazenie)
			if(wynik==y):
				ilosc_rozwiazan = ilosc_rozwiazan + 1 #M9
			ilosc_kombinacji=ilosc_kombinacji+1
			return 0
		else:
			if (naw_otwarty>naw_zamkniety):
				nawiasy = zamien_jeden_znak(nawiasy,naw_pozycja, ")")
				licz_wyrazenie(y,liczby,operatory,nawiasy,level_op,naw_pozycja+1,naw_otwarty,naw_zamkniety+1)
			if (naw_otwarty<Nop):
				nawiasy = zamien_jeden_znak(nawiasy,naw_pozycja, "(")
				licz_wyrazenie(y,liczby,operatory,nawiasy,level_op,naw_pozycja+1,naw_otwarty+1,naw_zamkniety)
	else:
	#M4
		operatory_nowe_plus = operatory + "+"
		licz_wyrazenie(y,liczby,operatory_nowe_plus,nawiasy,level_op-1,naw_pozycja,naw_otwarty,naw_zamkniety)
	
		operatory_nowe_minus = operatory + "-"
		licz_wyrazenie(y,liczby,operatory_nowe_minus,nawiasy,level_op-1,naw_pozycja,naw_otwarty,naw_zamkniety)
	
		operatory_nowe_mnoz = operatory + "*"
		licz_wyrazenie(y,liczby,operatory_nowe_mnoz,nawiasy,level_op-1,naw_pozycja,naw_otwarty,naw_zamkniety)
	return 0

def zagadka(liczby,y):
	Nliczb = len(liczby)
	Nop = Nliczb - 1
	nawiasy = ""
	global ilosc_kombinacji
	global ilosc_rozwiazan 
	for x in range(0,2*Nop):
		nawiasy = nawiasy + " "
	operatory = ""
	print("Znalezione rozwiazania zagadki dla liczb " + str(liczby)+" = " + str(y) + " to: ")
	licz_wyrazenie(y,liczby,operatory,nawiasy,Nliczb,0,0,0) #M2
	print("Przeszukano do tego celu "+str(ilosc_kombinacji)+" kombinacji, znaleziono "+str(ilosc_rozwiazan)+" rozwiazan")
	ilosc_kombinacji=0
	ilosc_rozwiazan =0
	print(" ")
	return 0


zagadka([1,2,3,4],0)  #M1

