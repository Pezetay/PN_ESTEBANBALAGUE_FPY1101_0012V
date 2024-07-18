import random
import csv
import math

# Lista de empleados
trabajadores = [
    {"nombre": "Juan Perez"},
    {"nombre": "Maria Garcia"},
    {"nombre": "Carlos Lopez"},
    {"nombre": "Ana Martinez"},
    {"nombre": "Pedro Rodriguez"},
    {"nombre": "Laura Hernandez"},
    {"nombre": "Miguel Sanchez"},
    {"nombre": "Isabel Gomez"},
    {"nombre": "Francisco Diaz"},
    {"nombre": "Elena Fernandez"}
]

# Asignación de sueldos aleatorios
sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    sueldos_menores = [trabajadores[i] for i in range(len(trabajadores)) if sueldos[i] < 800000]
    sueldos_medios = [trabajadores[i] for i in range(len(trabajadores)) if 800000 <= sueldos[i] <= 2000000]
    sueldos_mayores = [trabajadores[i] for i in range(len(trabajadores)) if sueldos[i] > 2000000]

    print("Sueldos menores a $800.000 TOTAL:", len(sueldos_menores))
    for i in range(len(trabajadores)):
        if sueldos[i] < 800000:
            print(f"Nombre empleado:     Sueldo: ")
            print(f"{trabajadores[i]['nombre']:20} ${sueldos[i]}")

    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len(sueldos_medios))
    for i in range(len(trabajadores)):
        if 800000 <= sueldos[i] <= 2000000:
            print(f"Nombre empleado:     Sueldo: ")
            print(f"{trabajadores[i]['nombre']:20} ${sueldos[i]}")

    print("\nSueldos superiores a $2.000.000 TOTAL:", len(sueldos_mayores))
    for i in range(len(trabajadores)):
        if sueldos[i] > 2000000:
            print(f"Nombre empleado:     Sueldo: ")
            print(f"{trabajadores[i]['nombre']:20} ${sueldos[i]}")

    print("\nTOTAL SUELDOS:", sum(sueldos))

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"Media geométrica de sueldos: ${sueldo_geom:.2f}")

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        for i in range(len(trabajadores)):
            descuento_salud = sueldos[i] * 0.07
            descuento_afp = sueldos[i] * 0.12
            sueldo_liquido = sueldos[i] - descuento_salud - descuento_afp
            writer.writerow([trabajadores[i]["nombre"], sueldos[i], descuento_salud, descuento_afp, sueldo_liquido])
            print(f"Nombre empleado: {trabajadores[i]['nombre']} Sueldo Base: ${sueldos[i]} Descuento Salud: ${descuento_salud:.2f} Descuento AFP: ${descuento_afp:.2f} Sueldo Líquido: ${sueldo_liquido:.2f}")

def salir_programa():
    print("Finalizando programa…")
    print("Desarrollado por Esteban Balague")
    print("RUT 19.343.705-2")

def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            asignar_sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
