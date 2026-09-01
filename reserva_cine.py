asientos= [[0 for _ in range(4)] for _ in range(3)]
print("---SISTEMA DE RESERVAS DE CINE ---")
fila = int(input("Ingrese el numero de fila (0 a 2): "))
columna = int(input("Ingrese el numero de columna (0 a 3): "))

if 0 <= fila < 3 and 0 <= columna < 4: 
    if asientos[fila][columna] == 0: 
        asientos[fila][columna] = 1
        print("\n!El asiento ha sido marcado como reservado con exito!")
    else:
        print("\n!Aviso! Este asiento ya se encuentra reservado.\n")
else:
    print("\n!Error! La fila o columna ingresada esta fuera del rango")
print("--- Estado Actual DE LA SALA ---")
for i in range(3):
     for j in range(4):
         print(asientos[i][j], end="\t")
     print()

