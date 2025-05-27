#libreria para luego obtener edades
from datetime import date
#funciones
def ingresar_dni():
    dni=input("Ingrese su numero de dni: ")
    return dni

def convierte_lista(dni):
    dni_en_lista=[]
    for i in dni:
        dni_en_lista.append(int(i))
    return dni_en_lista

def interseccion(conj_a, conj_b):
    conj_interseccion=[]
    for i in conj_a:
        for j in conj_b:
            if i==j:
                conj_interseccion.append(i)
    return conj_interseccion

def union(conj_a, conj_b):
    return list(set(conj_a + conj_b))

def diferencia(conj_a, conj_b):
    conj_diferencia=set(conj_a) - set(conj_b)
    return conj_diferencia

def diferencia_simetrica(conj_a, conj_b):
    conj_diferencia_simetrica=[]
    conj_diferencia_simetrica=list(diferencia(conj_a,conj_b)) +list(diferencia(conj_b, conj_a))
    return conj_diferencia_simetrica

def frecuencia_digito(conj,dni):
    print(f"Para el DNI {dni}:")
    frecuencia=[0]*10
    for i in conj:
        for j in range(10):
            if i==j:
                frecuencia[i]= frecuencia[i]+1
    mayor=0

    for i in range(10):
        if frecuencia[i]>mayor:
            mayor=frecuencia[i]
    for i in range(10):
        print(f"El numero {i} se repite {frecuencia[i]} veces ")

def suma_total(conj):
    suma=0
    for i in conj:
        suma=suma+i
    return suma

def buscar_digito(numero, conj_a, conj_b, conj_c, conj_d):
    if (numero in conj_a) and (numero in conj_b) and (numero in conj_c) and (numero in conj_d):
        print(f"El digito {numero} esta en todos los conjuntos!!!")
    else:
        print(f"El digito {numero} no esta presente en todos conjuntos")

def diversidad(dni, conj):
    if len(conj)>6:
        print(f"el DNI {dni} presenta diversidad numerica")
    else:
        print(f"El DNI {dni} no presenta diversidad numerica")

def ingreso_anios():
    anios=[]
    cantidad=int(input("Ingrese la cantidad de integrantes del grupo: "))
    for i in range (cantidad):
        anio=int(input(f"Ingresa el año de nacimiento de la persona nro {i+1}: "))
        anios.append(anio)
    return anios

def contar_par_impar(anios):
    pares=0
    impares=0
    for anio in anios:
        if anio%2==0:
            pares+=1
        else:
            impares+=1 
    return pares, impares

def grupo_z(anios):
    for anio in anios:
        if anio <= 2000:
            return False
    return True

def bisiesto(anio):
    #Un año es bisiesto si es divisible por 4 y no es divisible por 100 o si es divisible por 400
    return (anio%4==0 and anio%100 !=0) or (anio%400==0) 

def hay_bisiesto(anios):
    for anio in anios:
        if bisiesto(anio):
            return True
    return False

def obtener_edades(anios):
    anio_actual=date.today().year
    return [anio_actual-anio for anio in anios]

def producto_cartesiano(anios, edades):
    return[(a, e) for a in anios for e in edades]

#programa_principal
#solicita DNI
dni_1=ingresar_dni()
dni_2=ingresar_dni()
dni_3=ingresar_dni()
dni_4=ingresar_dni()

#CONVIERTE CADENA A LISTA
dni_1_lista=convierte_lista(dni_1)
dni_2_lista=convierte_lista(dni_2)
dni_3_lista=convierte_lista(dni_3)
dni_4_lista=convierte_lista(dni_4)

#CONVIERTE A CONJUNTOS
dni_1_conj=list(set(dni_1_lista))
dni_2_conj=list(set(dni_2_lista))
dni_3_conj=list(set(dni_3_lista))
dni_4_conj=list(set(dni_4_lista))

#MUESTRA CONJUNTOS
print(f"El conjunto A para el DNI {dni_1} es: ")
print(dni_1_conj)
print(f"El conjunto B para el DNI {dni_2} es: ")
print(dni_2_conj)
print(f"El conjunto C para el DNI {dni_3} es: ")
print(dni_3_conj)
print(f"El conjunto D para el DNI {dni_4} es: ")
print(dni_4_conj)
print("------------------------------------")
input()

#OPERACIONES ENTRE CONJUNTOS
print("OPERACIONES ENTRE CONJUNTOS A y B")
print(f"La interseccion entre los conjuntos {dni_1_conj} y {dni_2_conj} es: ",interseccion(dni_1_conj, dni_2_conj))
print(f"La union de los conjuntos  {dni_1_conj} y {dni_2_conj} es: ",union(dni_1_conj, dni_2_conj))
print(f"La diferencia entre los conjuntos {dni_1_conj} y {dni_2_conj} es: ",diferencia(dni_1_conj, dni_2_conj))
print(f"La diferencia simterica entre los conjuntos {dni_1_conj} y {dni_2_conj} es: ",diferencia_simetrica(dni_1_conj, dni_2_conj))
print("           ............           " )
print("OPERACIONES ENTRE CONJUNTOS C y D")
print(f"La interseccion entre los conjuntos {dni_3_conj} y {dni_4_conj} es: ",interseccion(dni_3_conj, dni_4_conj))
print(f"La union de los conjuntos  {dni_3_conj} y {dni_4_conj} es: ",union(dni_3_conj, dni_4_conj))
print(f"La diferencia entre los conjuntos {dni_3_conj} y {dni_4_conj} es: ",diferencia(dni_3_conj, dni_4_conj))
print(f"La diferencia simterica entre los conjuntos {dni_3_conj} y {dni_4_conj} es: ",diferencia_simetrica(dni_3_conj, dni_4_conj))
print("------------------------------------")
input()

#FRECUENCIA DE DIGITOS
print("REPITENCIA DE DIGITOS")
frecuencia_digito(dni_1_lista, dni_1)
frecuencia_digito(dni_2_lista, dni_2)
frecuencia_digito(dni_3_lista, dni_3)
frecuencia_digito(dni_4_lista, dni_4)
print(f"Para el DNI {dni_3} la suma total de los digitos es: {suma_total(dni_3_lista)}")
print(f"Para el DNI {dni_4} la suma total de los digitos es: {suma_total(dni_4_lista)}")
print("------------------------------------")
input()

#EVALUACION DE CONDICIONES LOGICAS

seleccion=int(input("Elija un digito (0 al 9) para buscar en los conjuntos: "))
print(f"Ud quiere saber si el numero {seleccion} esta en todos los conjuntos......")
buscar_digito(seleccion, dni_1_conj, dni_2_conj, dni_3_conj, dni_4_conj)
input()

print("DIVERSIDAD NUMERICA (conjunto de mas de 6 elementos)")
diversidad(dni_1, dni_1_conj)
diversidad(dni_2, dni_2_conj)
diversidad(dni_3, dni_3_conj)
diversidad(dni_4, dni_4_conj)
print(f"Para el DNI {dni_1} la suma total de los digitos es: {suma_total(dni_1_lista)}")
print(f"Para el DNI {dni_2} la suma total de los digitos es: {suma_total(dni_2_lista)}")
print(f"Para el DNI {dni_3} la suma total de los digitos es: {suma_total(dni_3_lista)}")
print(f"Para el DNI {dni_4} la suma total de los digitos es: {suma_total(dni_4_lista)}")
print("------------------------------------")
input()

#EVALUACION DE CONDICIONES LOGICAS

seleccion=int(input("Elija un digito (0 al 9) para buscar en los conjuntos: "))
print(f"Ud quiere saber si el numero {seleccion} esta en todos los conjuntos......")
buscar_digito(seleccion, dni_1_conj, dni_2_conj, dni_3_conj, dni_4_conj)
input()

print("DIVERSIDAD NUMERICA (conjunto de mas de 6 elementos)")
diversidad(dni_1, dni_1_conj)
diversidad(dni_2, dni_2_conj)
diversidad(dni_3, dni_3_conj)
diversidad(dni_4, dni_4_conj)
print("------------------------------------")
input()

#INGRESAR EDADES
lista_anios = ingreso_anios()
print("------------------------------------")
input()

#DETERMINAR PARES E IMPARES
pares, impares=contar_par_impar(lista_anios)
print(f"Numeros pares {pares}, numeros impares {impares}")
print("------------------------------------")
input()

#GRUPO Z
if grupo_z(lista_anios)==True:
    print("Grupo Z")
print("------------------------------------")
input()

#BISIESTO
if hay_bisiesto(lista_anios)==True:
    print("Tenemos un año especial")
    print("------------------------------------")
    input()

#EDADES
edades=obtener_edades(lista_anios)

#PRODUCTO CARTESIANO
producto=producto_cartesiano(lista_anios, edades)
print("Producto cartesiano: ")
for i in producto:
    print(i)