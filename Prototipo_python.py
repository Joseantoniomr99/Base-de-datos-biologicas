# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:10:36 2020

@author: Usuario
"""


import pymysql.cursors
import sys

connection = pymysql.connect(host='localhost',
                            user = 'root',
                            password = 'Jose150999',
                            db = 'base de datos',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)
print('connect succesfull')

Unir_Tablas = input('Intrduzca 1 si quiere realizar una consulta de varias tablas o 0 en caso de usar solo una tabla: ')

if(Unir_Tablas == '0'):
    Frase_Select = 'Select '
    Frase_Condicion = 'Where '
    Tabla = input('Introduzca el nombre dela tabla en la que quiere buscar información: ')
    Columna = input('Introduzca el nombre de la columna deseada')
    Frase_Select = Frase_Select + Columna  + " "

    Continuar_columnas = input('Introduzca 1 si quieres seleccionar mas columnas, en caso contrario 0: ')

    while Continuar_columnas == '1' :
        Columna = input('Introduzca el nombre de la columna en cuestión: ')
        Frase_Select = Frase_Select + "," + Columna + " "
        Continuar_columnas = input('Introduzca 1 si quieres seleccionar mas columnas, en caso contrario 0: ')
    
    Sintaxis_Where = 'where '
    Condicion = input('Introduzca la condicion deseada, 0 si no desea introducir ninguna: ')
    Si_Condicion = 0
    if Condicion != '0':
        Sintaxis_Where = Sintaxis_Where + Condicion + " "
        Si_Condicion = 1
    
    while Condicion != '0':
        Condicion = input('Introduzca otra condicion, 0 en caso de no querer introducir ninguna: ')
        if Condicion != '0':
            Sintaxis_Where = Sintaxis_Where +  "," + Condicion + " "
            
    if Si_Condicion == 1:
        Query = Frase_Select + "from " + Tabla + Sintaxis_Where
    else:
        Query = Frase_Select + "from " + Tabla
    try:
        with connection.cursor() as cursor:
                    cursor.execute(Query)
                    print()
                    for row in cursor:
                        print(row)
                    print()
    finally:
                # Close connection.
                connection.close()
    sys.exit()
    
    

else:
    Frase_Select = 'Select '
    Tablas = []
    Tabla = input('Introduzca el nombre de las tablas que quiere usar, 0 para terminar(No intrduzca tablas de enlace): ')
    Tablas.append(Tabla)
    while Tabla != '0':
        Tabla = input('Introduzca el nombre de las tablas que quiere usar, 0 para terminar: ')
        if Tabla != '0':
            Tablas.append(Tabla)
    
    proteinas = 0
    genes = 0
    enfermedades = 0
    sintomas = 0
    
    for i in range(len(Tablas)):
        if Tablas[i] == "proteinas":
            proteinas = 1
        elif Tablas[i] == "genes":
            genes = 1
        elif Tablas[i] == "enfermedades":
            enfermedades = 1
        elif Tablas[i] == "sintomas":
            sintomas = 0
            
    Sintaxis_From = "from "
    
    if enfermedades == 1 & genes == 1:
        Sintaxis_From = Sintaxis_From + "enfermedades e inner join enfermedad_genes eg on e.idenfermedades = eg.enf_id inner join genes g on eg.gen_id = g.Id_gen "
        if proteinas == 1:
            Sintaxis_From = Sintaxis_From + "inner join genes_proteinas gp on g.Id_gen = gp.id_genes inner join proteinas p on gp.id_proteinas = p.Idproteinas "
            if sintomas == 1:
                Sintaxis_From = Sintaxis_From + "inner join enfermedades_sintomas es on e.idenfermedades = es.id_enfermedades inner join sintomas s on es.id_sintomas = s.id_sintomas "
                
            
        elif sintomas == 1:
            Sintaxis_From = Sintaxis_From + "inner join enfermedades_sintomas es on e.idenfermedades = es.id_enfermedades inner join sintomas s on es.id_sintomas = s.id_sintomas "
    elif enfermedades == 1 & sintomas == 1:
         Sintaxis_From = Sintaxis_From + "enfermedades e inner join enfermedades_sintomas es on e.idenfermedades = es.id_enfermedades inner join sintomas s on es.id_sintomas = s.id_sintomas "
    elif enfermedades == 1:
         Sintaxis_From = Sintaxis_From + "enfermedades "
    elif genes == 1 & proteinas == 1:
         Sintaxis_From = Sintaxis_From + "genes g inner join genes_proteinas gp on g.Id_gen = gp.id_genes inner join proteinas p on gp.id_proteinas = p.Idproteinas "
    elif sintomas == 1:
         Sintaxis_From = Sintaxis_From + "sintomas "
    elif genes == 1:
         Sintaxis_From = Sintaxis_From + "genes "
    elif proteinas == 1:
         Sintaxis_From = Sintaxis_From + "proteinas "
    
    Columna = input('Introduzca el nombre de la columna deseada(especifique la tabla a la que pertenence dicha columna, por ejemplo si quiero el id de enfermedades sería e.idenfermedades): ')
    Frase_Select = Frase_Select + Columna + " "
    
    Continuar_columnas = input('Introduzca 1 si quieres seleccionar mas columnas, en caso contrario 0: ')

    while Continuar_columnas == '1' :
        Columna = input('Introduzca el nombre de la columna deseada(especifique la tabla a la que pertenence dicha columna, por ejemplo si quiero el id de enfermedades sería e.idenfermedades): ')
        Frase_Select = Frase_Select +  ","+ Columna + " "
        Continuar_columnas = input('Introduzca 1 si quieres seleccionar mas columnas, en caso contrario 0: ')
    
    Sintaxis_Where = 'where '
    Condicion = input('Introduzca la condicion deseada, 0 si no desea introducir ninguna')
    Si_Condicion = 0
    if Condicion != '0':
        Sintaxis_Where = Sintaxis_Where + Condicion + " "
        Si_Condicion = 1
    
    while Condicion != '0':
        Condicion = input('Introduzca otra condicion, 0 en caso de no querer introducir ninguna:')
        if Condicion != '0':
            Sintaxis_Where = Sintaxis_Where +  "," + Condicion + " "
            
    if Si_Condicion == 1:
        Query = Frase_Select + Sintaxis_From + Condicion
    else:
        Query = Frase_Select + Sintaxis_From
        
    try:
        with connection.cursor() as cursor:
                    cursor.execute(Query)
                    print()
                    for row in cursor:
                        print(row)
                    print()
    finally:
                # Close connection.
                connection.close()
    sys.exit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        