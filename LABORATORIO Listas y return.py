# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:50:08 2019

@author: BLUEIT-PARTICIPANTE
"""
# definicion de funcion
cal1=0
cal2=0
cal3=0

def isyearleap(year):
    cal1=yr%4
    cal2=yr%100
    cal3=yr%400
    if cal1 == 0:
        if cal2 != 0:
            return True
        elif cal2 == 0 and cal3 == 0:
            return True
        elif cal2 == 0 and cal3 != 0:
            return False
        elif cal2 == 0:
            return False
        elif cal2 != 0:
            return False
    else:
        return False
    
#inicio de codigo

testData = [1900,2000,2016,1987]
# testResult = [False,True,True,False] "[False,True,False,True] ERROR

print ("\n""ESTE CODIGO VERIFICA SI UN AÑO ES BISIESTO","\n")

for i in range(len(testData)):
    yr=testData[i]
    print(yr,"->",end=" ")
    print(isyearleap(i))
        
