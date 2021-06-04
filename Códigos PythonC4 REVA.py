
#OPERACIONES CON LISTAS= CONCATENACIÓN Y MULTIPLICACIÓN
FRUTAS=['banana','pera']
VERDURAS=['papa','cebolla']
COMPRA_1=FRUTAS+VERDURAS
COMPRA_2=FRUTAS*2+VERDURAS
print(COMPRA_1)
print(COMPRA_2)

print('-----------------------------------------------------------------------------------')

#OPERACIONES CON LISTAS= CONCATENACIÓN DE INT
#!PROBAR MULTIPLICACIÓN POR ESCALAR (ESCALAR SIGNIFICA UNA CONSTANTE ENTERA)
NUMEROS_PARES=[2,4,6,8,10]
NUMEROS_IMPARES=[1,3,5,7,9]
NUMEROS_10=NUMEROS_PARES+NUMEROS_IMPARES
print(NUMEROS_10)

print('-----------------------------------------------------------------------------------')
#OPERACIONES CON LISTAS= AÑADIR ELEMENTOS A UNA LISTA, DESDE OTRA
                        #LISTA SIN CAMBIAR EL NOMBRE DE LA VARIABLE
NUMEROS_PARES=[2,4,6,8,10]
NUMEROS_IMPARES=[1,3,5,7,9]
NUMEROS_PARES+=NUMEROS_IMPARES
print(NUMEROS_PARES)

print('-----------------------------------------------------------------------------------')
#OPERACIONES CON LISTAS= AGREGAR ELEMENTOS CON APPEND
NUMEROS_PARES=[2,4,6,8,10] 
NUMEROS_PARES.append([12,14,16])
print(NUMEROS_PARES)

print('-----------------------------------------------------------------------------------')
#OPERACIONES CON LISTAS= AGREGAR A UNA LISTA, ELEMENTOS DE OTRA
                        #LISTA, CON extend SIN CAMBIAR EL NOMBRE DE VARIABLE
NUMEROS_1=[2,4,6,8,10]
NUMEROS_2=[1,3,5,7,9]
NUMEROS_1.extend(NUMEROS_2)
print(NUMEROS_1)

print('-----------------------------------------------------------------------------------')
#OPERACIONES CON LISTAS= AGREGAR ELEMENTO CON CON INSERT+POSICIÓN
RANKING_IMDB=['Shawshank..', 'El Padrino I', 'Dark Knight']
RANKING_IMDB.insert(2,'El Padrino II')
print(RANKING_IMDB)

print('-----------------------------------------------------------------------------------')
#ELIMINAR UN ELEMENTO DE LA LISTA, SABIENDO SU POSICIÓN:
RANKING=['Shawshank..', 'El Padrino I','El Padrino II', 'Dark Knight']
RANKING.pop(0)
print(RANKING)

RANKING=['Shawshank..', 'El Padrino I','El Padrino II', 'Dark Knight']
del RANKING[0]
print(RANKING)

print('-----------------------------------------------------------------------------------')
#recorrer listas con el comando for, ejemplo 1
CIENTIFICOS_POSTA=['Tesla','Ramanujan','Schrodinger','Edison','Houssay','Milstein']
for x in CIENTIFICOS_POSTA:
    if x=='Houssay' or x=='Milstein':
        print(x,'es un científico argentino')
print('Fin')

print('-----------------------------------------------------------------------------------')

#recorrer listas con el comando for , ejemplo 2
CIENTIFICOS_POSTA=['Tesla','Ramanujan','Schrodinger','Edison','Houssay']
for x in CIENTIFICOS_POSTA:
    if x=='Edison':
        CIENTIFICOS_POSTA.remove(x)
        print('Se hizo justicia')
print(CIENTIFICOS_POSTA)

print('-----------------------------------------------------------------------------------')

#recorrer lista con el comando for ejemplo 3
CIENTIFICOS_POSTA=['Tesla','Ramanujan','Schrodinger','Edison','Houssay']
for x in CIENTIFICOS_POSTA:
   if x == 'Edison':
     continue
   else:
     print(x)

print('-----------------------------------------------------------------------------------')

#recorrer listas con for ejemplo 4
CIENTIFICOS_POSTA=['Tesla','Ramanujan','Schrodinger','Edison','Houssay']
for x in CIENTIFICOS_POSTA:
   if x == 'Edison':
     print(x,'vos te colaste en la lista')
   else:
     print(x)

print('-----------------------------------------------------------------------------------')

#CONTAR ELEMENTOS DE LISTAS O caracteres EN CADENAS CON EL COMANDO len()
NOTAS_ALUMNOS=[4,5,8,5,8,10,10,9,6]
PROMEDIO=sum(NOTAS_ALUMNOS)/len(NOTAS_ALUMNOS) #el comando sum() solo funciona con variables numéricas
print(PROMEDIO)                                #notar que si bien la lista tiene números enteros, la división siempre
                                               #resulta con variable flotante, por más que los elementos sean enteros

print('-----------------------------------------------------------------------------------')

#CONTAR CARACTERES NUMÉRICOS (FORMATO STR) CON LEN() -> CODIFICACIÓN
CBU='2850590940090418135201'                     #FORMATO CADENAS
if len(CBU)==22:                                 #formato numérico
    print('CBU bien cargado')
else:
    print('Error en la carga de CBU')

print('-----------------------------------------------------------------------------------')






a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


a = [1, 1, 1]
c = a*3
print(c)

print('-----------------------------------------------------------------------------------')
numeros=[0,1,'uno',3.5,4]
print('uno' in numeros)
print(7 in numeros)
print(not 5 in numeros)

#lista_de_pelis=[["Martin McDonagh", ["In Bruges", 2008]],["Bryan Singer", ["The Usual Suspects", 1996]],[["Dorota Kobiela", “Hugh Welchman”],["Loving Vincent", 2017]]]
