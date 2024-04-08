# Función para pedir el nombre al usuario y saludar
def saludo_personalizado():
    nombre = input("Por favor, ingresa tu nombre: ")  # Captura la entrada del usuario
    print(f"Hola, {nombre}! Bienvenido/a.")  # Muestra el mensaje de saludo personalizado

# Llamar a la función
saludo_personalizado()


# Función para contar hasta un número específico
def contador_numeros():
    numero = int(input("Ingresa un número entero: "))  # Captura la entrada y conviértela a entero
    for i in range(1, numero + 1):  # Bucle desde 1 hasta el número ingresado
        print(i)  # Imprime cada número

# Llamar a la función
contador_numeros()

# Función para realizar operaciones aritméticas básicas
def calculadora_basica():
    num1 = float(input("Ingresa el primer número: "))  # Primer número
    num2 = float(input("Ingresa el segundo número: "))  # Segundo número
    operacion = input("Ingresa la operación (suma, resta, multiplicación, división): ")  # Operación deseada

    # Realizar la operación y mostrar el resultado
    if operacion == "suma":
        print(f"El resultado de {num1} + {num2} es {num1 + num2}")
    elif operacion == "resta":
        print(f"El resultado de {num1} - {num2} es {num1 - num2}")
    elif operacion == "multiplicación":
        print(f"El resultado de {num1} * {num2} es {num1 * num2}")
    elif operacion == "división":
        if num2 != 0:
            print(f"El resultado de {num1} / {num2} es {num1 / num2}")
        else:
            print("Error: División por cero no permitida.")
    else:
        print("Operación no reconocida. Por favor, intenta de nuevo.")

# Llamar a la función
calculadora_basica()