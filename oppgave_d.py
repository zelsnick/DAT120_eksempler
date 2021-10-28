# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:08:42 2021

@author: Nicol
"""

from oppgave_b import Sporsmaal

def lesefil():    
    liste=[]
    with open("sporsmaalsfil.txt", "r",encoding="UTF8" ) as fila:
        for linje in fila:
            linje = linje.strip()
            linje = linje.split(":")
            question = linje[0]
            rett_svar = int(linje[1])
            alternativ = linje[2]
            
            
            alternativ = alternativ.replace("[", "")
            alternativ = alternativ.replace("]", "")
            alternativ = alternativ.split(",")
            liste.append(Sporsmaal(question, rett_svar, alternativ))
            
        return liste
#            return (question, rett_svar, alternativ)
        
    
    
#            slutt = linje.find("]")+1
#            ny = linje[0 : slutt]
#            liste = ny
#            print(alternativ)
    
#x = lesefil()          
#print(x)


if __name__ == "__main__":
    teller1 = 0
    teller2 = 0
    liste_objekt = lesefil()
    for spm in liste_objekt:
        print(spm)
        spiller1 = int(input("Spiller1: hva er svaret?: "))
                        
        spiller2 = int(input(" Spiller2: hva er svaret?: "))
        

        print(f"korekt svar er: {spm.korekt_svar_tekst()}")
                
        if spm.sjekk_svar(spiller1):
            print ("svar er korekt")
            teller1 += 1
            print(f"spiller1 har {teller1} korekt svar!")
        else:
            print("feil svar")
        if spiller2 == spm.rett_svar:
            print ("svar er korekt")
            teller2 += 1
            print(f"spiller 2 gar {teller2} korekt svar!")
        else:
            print("feil svar")
        print()
    print(f"Spiller 1 fikk {teller1}/{len(liste_objekt)}")