# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:17:50 2019

@author: BLUEIT-PARTICIPANTE
"""
#definicion de funcion
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
    
#inicio codigo
    
print("\n","ESTE CODIGO VERIFICA SI UN NUMERO ES PRIMO EN UN RANGO","\n")

limsup=input("Indique el valor maximo: ")
print("\n") 
for i in range(1,int(limsup)+1):
    isPrime(i)
    if isPrime(i) is True:
        print(i,"Es número Primo") 
    else:
        print(i,"No es número Primo") 
        
