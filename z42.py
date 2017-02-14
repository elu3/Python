def dziel_wyrazenie(lista): 
    if(len(lista)>1): 
        for i in range(1,len(lista)): 
            for a1 in dziel_wyrazenie(lista[:i]): 

                for a2 in dziel_wyrazenie(lista[i:]):
                    yield '('+a1+'*'+a2+')' 
                    yield '('+a1+'-'+a2+')'
                    yield '('+a1+'+'+a2+')'
    else:
	yield str(lista[0])

def drukuj_linijke(lista,y):
    for w in dziel_wyrazenie(lista): 
        if(eval(w)==y): 
            yield w + ' = ' + str(y)

def zagadka(lista,y): 
	for rozwiazanie in drukuj_linijke(lista,y): 
		print(rozwiazanie)	

zagadka([1,2,3,4],0)


