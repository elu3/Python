def kon(l):
  
   arabic=[1, 4, 5, 9, 10, 40, 50, 90, 100,400, 500, 900, 1000] 
   roman=["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"] 
   solution=""
   
   for i in range (12,0,-1):
     
      while(l>=arabic[i]):
         l-=arabic[i]
         solution+=roman[i]
   print(solution)
   
   
kon(7)



