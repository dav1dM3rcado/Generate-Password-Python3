import random

def generate_password():

        capital_letter = ['A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'x', 'y', 'z']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        characters = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
        '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°',
        '^', '&', '$', '#', '"']
        characters = capital_letter + lower_case + characters + numbers
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
