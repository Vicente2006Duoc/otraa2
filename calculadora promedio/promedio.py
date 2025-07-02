Bienvenida = input("¡Hola!Ingrese su nombre porfavor: ")
print(f"Bienvenido {Bienvenida}! Este es una calculadora de promedios de notas.")
notas = []
cantidad = int(input("ingreese la cantidad de notas: "))
for i in range(cantidad):
    nota = float(input(f"ingrese la nota numero {i + 1} :"))
    notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    print("el promedio final es {promedio:2f}")