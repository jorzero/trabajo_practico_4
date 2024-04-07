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