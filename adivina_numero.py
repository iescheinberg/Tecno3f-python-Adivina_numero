import random

# Mauro Rodriguez
# Guillermo Rodriguez

# Generamos el numero
secret_number = random.randint(1, 50)
attempts = 0

# Aviso al usuario
print("*** ADIVINA EL NÚMERO ***")
print("Reglas:\n1- Debes adivinar el número comprendido entre 1 y 50.\n2- Tienes 5 intentos para adivinarlo.\n3- El juego termina cuandso adivines el número o se te terminan tus 5 intentos.\nBUENA SUERTE!💪")


# Codigo del juego
while attempts < 5:
    attempt = int(input("Elige tu número: "))
    attempts += 1
    
    if attempt < secret_number:
        print("Tu número es muy bajo 👇. Intenta de nuevo! ")
    elif attempt > secret_number:
        print("Tu número es muy alto 👆. Intenta de nuevo! ")
    else:
        print(f"¡Felicidades!🥳, adivinaste en el {attempts} intento.")

if attempts == 5 and attempt != secret_number:
    print(f"Lo siento has usado tus 5 intentos 😞\nEl numero secreto era {secret_number} \nMejor suerte la proxima!💪")
