print("Bienvenido, este es un menú que pregunta al usuario qué quiere hacer y muestra submenús")
menu = 0
while menu != 3:
    print("MENÚ PRINCIPAL:")
    print("1. Calculadora.")
    print("2. IMC o Rango de edad.")
    print("3. Salir.")

    menu = input("¿Qué opción desea ejecutar?: ")

    # Validación para que solo acepte números
    menu_val = True
    for i in menu:
        if i < "0" or i > "9":
            menu_val = False

    while menu_val == False:
        print("Error: solo números")
        menu = input("¿Qué opción desea ejecutar?: ")
        menu_val = True
        for i in menu:
            if i < "0" or i > "9":
                menu_val = False

    menu = int(menu)

    # Opciones de la Calculadora:
    if menu == 1:
        sub = 0
        while sub != 6:
            print("\nSubmenú calculadora:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Potenciación")
            print("6. Volver")

            sub = input("Seleccione una opción: ")

            # Validación para que solo permita números:
            sub_val = True
            for i in sub:
                if i < "0" or i > "9":
                    sub_val = False

            while sub_val == False:
                print("Error: solo números")
                sub = input("Seleccione una opción: ")
                sub_val = True
                for i in sub:
                    if i < "0" or i > "9":
                        sub_val = False

            sub = int(sub)

            if sub >= 1 and sub <= 5:
                a = int(input("Digite el primer número: "))
                b = int(input("Digite el segundo número: "))

                if sub == 1:
                    print("Resultado:", a + b)
                elif sub == 2:
                    print("Resultado:", a - b)
                elif sub == 3:
                    print("Resultado:", a * b)
                elif sub == 4:
                    if b != 0:
                        print("Resultado:", a / b)
                    else:
                        print("No se puede dividir entre 0")
                elif sub == 5:
                    print("Resultado:", a ** b)

            elif sub != 6:
                print("ERROR: Opción inválida")
    elif menu == 2: # Opciones de si es IMC o rango:
        sub2 = 0
        while sub2 != 3:
            print("\nSubmenú IMC o Edad:")
            print("1. Calcular IMC")
            print("2. Rango de edad")
            print("3. Volver")

            sub2 = input("Seleccione una opción: ")

            # Validación para que solo acepte números:
            sub2_val = True
            for i in sub2:
                if i < "0" or i > "9":
                    sub2_val = False

            while sub2_val == False:
                print("Error: solo números")
                sub2 = input("Seleccione una opción: ")
                sub2_val = True
                for i in sub2:
                    if i < "0" or i > "9":
                        sub2_val = False

            sub2 = int(sub2)

            if sub2 == 1:
                peso = float(input("Ingresa tu peso en kg: "))
                altura = float(input("Ingresa tu altura en metros: "))
                imc = peso / (altura ** 2)
                print("Tu IMC es:", imc)

                if imc < 18.5:
                    print("Estás en Bajo peso.")
                elif imc < 25:
                    print("Tu IMC es Normal.")
                elif imc < 30:
                    print("Estás en Sobrepeso.")
                else:
                    print("Tienes Obesidad.")

            elif sub2 == 2:
                edad = input("Ingrese su edad: ")

                # Validación para que solo acepte números
                edad_val = True
                for i in edad:
                    if i < "0" or i > "9":
                        edad_val = False

                while edad_val == False:
                    print("ERROR: solo números.")
                    edad = input("Ingrese su edad: ")
                    edad_val = True
                    for i in edad:
                        if i < "0" or i > "9":
                            edad_val = False

                edad = int(edad)

                if edad < 12:
                    print("eres un Niño.")
                elif edad < 18:
                    print("Eres un Adolescente.")
                elif edad < 60:
                    print("Eres un Adulto.")
                else:
                    print("eres un Adulto mayor.")

            elif sub2 != 3:
                print("ERROR: Opción inválida.")
    elif menu == 3:
        print("Hasta luego.")
    else:
        print("EEROR: Opción inválida.")