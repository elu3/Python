import sys
import re

def drukuj_info():
	print("Choose a command and confirm it using Enter")
	print("List of commands:")
	print("insert node ID")
	print("delete node ID")
	print("insert arc ID from ID1 to ID2")
	print("delete arc ID")
	print("nodes")
	print("arcs")
	print("path from ID1 to ID2")
	print("exit")
	print("print")
	print("info")


def wstaw_luk(graf,od_wezla,do_wezla,ID_luku):
	if not((od_wezla)in graf):
		print("Start Node doesn't exist!")
		return -1
	if not((do_wezla)in graf):
		print("End Node doesn't exist!")
		return -1
	for klucz in graf: #id of arc not use
		for wezel in graf[klucz]:
			if (wezel[1]==ID_luku):
				print("Arc ID already exist")
				return -1
	if not ((od_wezla)in graf):#if no node, put it
		graf[od_wezla].append([do_wezla,ID_luku])
		return 0
	for wezel in graf[od_wezla]:
		if (wezel[0]==do_wezla):
			print("Graph already have arc from "+od_wezla+" to "+do_wezla)
			return -1
	graf[od_wezla].append([do_wezla,ID_luku])
	return 0
 
 
def usun_luk(graf, ID_luku):
	for klucz in graf:
		for wezel in graf[klucz]:
			if (wezel[1]==ID_luku):
				graf[klucz].remove(wezel)	
				return 0	
	print("Nic nie usunieto, bo nie ma luku o ID: " + ID_luku)	
	return -1 


def wstaw_wezel(graf,nazwa):
	if ((nazwa)in graf):
		print("Wezel "+nazwa+" juz istnieje w grafie !")
	else:
		graf[nazwa] = []


def usun_wezel(graf,nazwa):
	if ((nazwa)in graf):#czy isnieje
		for klucz in graf.keys():#usun wszystkie luki prowadzace do usuwanego wezla z innych lukow
			for wezel in graf[klucz]:
				if(wezel[0]==nazwa):
					graf[klucz].remove(wezel)
		del graf[nazwa]#usun luk i wszystkie wezly wychodzace z niego
		return 0
	else:
		print("Nie ma wezla "+nazwa+" w grafie !")
		return -1

#backtrace
def znajdz_jakas_sciezke(graf, start, koniec, sciezka=[]):# start- wezel start
	sciezka = sciezka + [start]
	if start == koniec:# np pol z A do A
		return sciezka
	if not ((start)in graf):
		return False
	if(graf[start]):# lista graf[start] niepusta
		for wezel in graf[start][0]:
			if wezel not in sciezka:
				nowasciezka = znajdz_jakas_sciezke(graf, wezel, koniec, sciezka)
				if nowasciezka:
					return nowasciezka
	return False


def drukuj_wezly(graf):
	print("Wezly w grafie: ")
	if len(graf)>0:	
		for klucz in graf.keys():
			sys.stdout.write(klucz+" ")# drukowanie w tej samej linice
		print("")


def drukuj_luki(graf):
	print("Luki w grafie: ")
	if len(graf)>0:
		for klucz in graf.keys():
			for polaczenie in graf[klucz]:
				print("Luk od "+klucz+" do "+ polaczenie[0]+" o ID: "+polaczenie[1])
				

#przeanalizuj komende uzytkownika i wywolaj odpowiednia funkcje
def wykonaj_komende(tekst_uzytkownika, graf):
	rozpoznano = False
	if(tekst_uzytkownika == "exit"):
		rozpoznano = True
		return True
	if(tekst_uzytkownika=="nodes"):
		rozpoznano = True
		drukuj_wezly(graf)
	if(tekst_uzytkownika=="arcs"):
		rozpoznano = True
		drukuj_luki(graf)
	if(tekst_uzytkownika.startswith("insert node ")):
		rozpoznano = True
		wstaw_wezel(graf,tekst_uzytkownika["insert node ".__len__():])# dodaje wezel np A, przy insert node A
	if(tekst_uzytkownika.startswith("delete node ")):
		rozpoznano = True
		usun_wezel(graf,tekst_uzytkownika["delete node ".__len__():])#od dlugosci lancucha do konca
	if(tekst_uzytkownika.startswith("delete arc ")):
		rozpoznano = True
		usun_luk(graf,tekst_uzytkownika["delete arc ".__len__():])
	if(tekst_uzytkownika.startswith("insert arc ")):
		rozpoznano = True
		ID = re.findall(r"(?<=insert arc )(.*)(?= from)",tekst_uzytkownika)# luk o nazwie, re.findall-znajdz
		ID1= re.findall(r"(?<=from )(.*)(?= to)",tekst_uzytkownika)# z wezla
		ID2= re.findall(r"(?<=to )(.*)",tekst_uzytkownika)#wyrazenia regularne do wezla
		if (len(ID)>0 and len(ID1)>0 and len(ID2)>0):
			wstaw_luk(graf,ID1[0],ID2[0],ID[0])# 3 listy 1 elementowe
	if(tekst_uzytkownika.startswith("path from ")):
		rozpoznano = True
		ID1= re.findall(r"(?<=from )(.*)(?= to)",tekst_uzytkownika)#wez tekst pomiedzy "from " a " to" - wazna spacja
		ID2= re.findall(r"(?<=to )(.*)",tekst_uzytkownika)
		if(((ID1[0] in graf)) and ((ID2[0] in graf))):
			if(len(ID1)>0 and len(ID2)>0):
				sciezka = znajdz_jakas_sciezke(graf,ID1[0],ID2[0])
				if(sciezka==False):
					print("Wrong path")
				else:
					for element in sciezka:
						sys.stdout.write(element+" ")# w 1 linice drukuj
					print("")
	if(tekst_uzytkownika=="print"):
		rozpoznano = True
		print(graf)
	if(tekst_uzytkownika == "info"):
		rozpoznano = True
		drukuj_info()
	if ((not rozpoznano) and ( not (tekst_uzytkownika == "") )):
		print("Bad command!")
	return False


def glowna_petla(graf):
	skonczono = False
	while(not skonczono):
		wpisany_tekst_uzytkownika=input('Write command : ')
		skonczono = wykonaj_komende(wpisany_tekst_uzytkownika, mojgraf)
	return 0
	

#glowne wejscie do programu
#ustaw poczatkowo pusty graf
mojgraf = {}
#przykladowa struktura grafu - jako slownik
#My graph = {	  
#            'A': [['B', 'ID_A->B'], ['C', 'ID_A->C'], ['D', 'ID_A->D']],
#            'B': [['C', 'ID_B->C'], ['D', 'ID_B->D']],
#            'C': [['D', 'ID_C->D']],
#            'D': [['E', 'ID_D->E']],
#            'E': [['F', 'ID_E->F']],
#            'F': [['B', 'ID_F->B']]
#       }

drukuj_info()

glowna_petla(mojgraf)
