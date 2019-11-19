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

"""def dayOfYear(year, month, day): 

mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
           "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
"""
dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
dias_mes_bi=[31,29,31,30,31,30,31,31,30,31,30,31]
yr=0
mo=0
    

#inicio de codigo

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testDate = [2000,3,18]

print ("\n""ESTE CODIGO DEVUELVE EL NUMERO DE DIAS DE UNA AÑO-MES DESDE EL INICIO DE AÑO HASTA LA FECHA DADA","\n")

yr = testDate[0]
mo = testDate[1]
dy = testDate[2]
dy_acum = 0

if isyearleap(yr) is True:
    for i in range (mo-1):
        dy_acum = dias_mes_bi[i]+dy_acum
    dy_acum = dy_acum+dy
    print(yr, "es año bisiesto","el número de dias hasta la fecha son: ",dy_acum,end="\n")  
else: 
    for i in range (mo-1):
        dy_acum = dias_mes[i]+dy_acum
        print(dy_acum,end="\n")
    dy_acum = dy_acum+dy
    print(yr, "es año no bisiesto","el número de dias hasta la fecha son: ",dy_acum,end="\n")
