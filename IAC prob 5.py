#Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească
#cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion.
#Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească
#răspunsul mai repede.

nr= int(input("dati numarul lui Ion: "))
lista=[nr-2,nr-1,nr,nr+1,nr+2]
print("Vasile va spune: ",lista,sep="\n")