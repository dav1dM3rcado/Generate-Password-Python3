import random
import string

def generate_password():

        characters = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
        password = []
        numbers_of_chartes = int(input("Por favor Digite el tamaño de la contraseña(Maximo 15, minimo 8): "))
        for i in range(numbers_of_chartes):
            if numbers_of_chartes > 7  and numbers_of_chartes < 16:
                characters_random = random.choice(characters)
                password.append(characters_random)
            else:
                print("Ingresaste un numero NO válido.")
                run()
        password = ''.join(password)
        return password
def run():
    password = generate_password()
    print ("Tu nueva contraseña es : " + password)
    exit()
if __name__ == '__main__':
        run()
