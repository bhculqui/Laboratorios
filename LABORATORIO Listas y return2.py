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
mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
           "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
dias_mes_bi=[31,29,31,30,31,30,31,31,30,31,30,31]
yr=0
mo=0
    
#inicio de codigo

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

print ("\n""ESTE CODIGO DEVUELVE EL NUMERO DE DIAS DE UNA AÑO-MES","\n")

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    mes= testMonths[i]
    if isyearleap(yr) is True:
        print(yr, "es año    bisiesto","el mes",mo,"tiene",dias_mes[mo-1],end="\n")
    else: 
        print(yr, "es año no bisiesto","el mes",mo,"tiene",dias_mes[mo-1],end="\n")
