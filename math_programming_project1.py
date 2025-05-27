#Menu de inicio para el usuario
print("Simulador de Sumador de 1 Bit")
print("Ingresa dos bits binarios que quieras sumar (0 o 1)")

#Ingreso del primer bit
bit1=int(input("Primer bit: "))

#Debemos asegurarnos de que el usuario ingrese un numero valido
while bit1!=0 and bit1!=1:
    print("Ingrese un bit valido (1 o 0)")
    bit1=int(input("Primer bit: "))

#Ingreso del segundo bit
bit2=int(input("Segundo bit: "))

#Nuevamente debemos chequear que el numero sea valido
while bit2!=0 and bit2!=1:
    print("Ingrese un bit valido (1 o 0)")
    bit2=int(input("Segundo bit: "))

#Calculo de la suma y carry
if bit1!=bit2: 
    suma=1
else:
    suma=0

if bit1==1 and bit2==1: 
    carry=1
else:
    carry=0

#Mostrar Resultado
print("Resultado:")
print(f"Bit de suma:{suma}")
print(f"bit de carry: {carry}")