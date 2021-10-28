# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:09:06 2021

@author: Nicol
"""

class Sporsmaal:
    def __init__(self, sporsmaal, rett_svar, alternativ):
       
        self.sporsmaal = sporsmaal
        self.rett_svar = int(rett_svar)
        self.alternativ = alternativ
        
    def sjekk_svar(self, svar_avgitt):
        if svar_avgitt == self.rett_svar:
            print ("Svaret er korrekt")
            return True
        else:
            print ("feil")
            return False
    
    def __str__(self):
        temp = self.sporsmaal
        for i in range(len(self.alternativ)):
        
            temp += "\n" + str(i)
            
            temp += self.alternativ[i]
        return temp
        
    def korekt_svar_tekst(self):
        
        return self.alternativ[int(self.rett_svar)]
        
        
        
        
if __name__ == "__main__":        
    sporsmaal = "Hva er hovedstaden i norge?" 
    alternativer = ["oslo", "stocholm", "tokyo", "oslo"]
    tall = 1
    
    spm3 = Sporsmaal(sporsmaal, tall, alternativer)
    print(spm3)
    print(spm3.korekt_svar_tekst())