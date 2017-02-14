def ileDniDo (dzien,miesiac,rok):
    def przestepny (R):
        return (R%4==0) and (R%100!=0) or (R%400==0)
    def dniWRoku (R):
        if przestepny (R):
            return 366
        else:
            return 365
    pelneLata=0
    for R in range (1,rok):
        pelneLata+=dniWRoku (R)
    def dniWMiesiacu (M):
            if (M==1) or (M==3) or (M==5) or(M==7) or (M==8) or (M==10) or (M==12):
                return 31
            elif (M==4) or(M==6) or(M==9)or(M==11):
                return 30
            elif (M==2):
                 if przestepny (rok):
                     return 29
                 else:
                        return 28
    pelneMiesiace=0
    for M in range (1,miesiac):
                pelneMiesiace+=dniWMiesiacu(M)
    return pelneLata+pelneMiesiace+dzien-1
print ('dni: ')
print (ileDniDo (1,1,1))
