#/usr/bin/python3

import random
import string

flag_caracteres=input("Desea que la contraseña contenga caracteres especiales? si/no" + " ")

if flag_caracteres == "si" or flag_caracteres == "no":
    largo=int(input("De cuantos caracteres desea su contraseña? Por favor ponga numeros enteros Ej: 1, 20, 300, Etc." + " " ))
    con_simbolos= "!@#$%^&*" + string.ascii_lowercase + string.digits + "!@#$%^&*"
    sin_simbolos= string.ascii_lowercase + string.digits

    if flag_caracteres == "si":
        contraseña = ''.join(random.choice(con_simbolos) for _ in range(largo))
    else:
        contraseña = ''.join(random.choice(sin_simbolos) for _ in range(largo))

    print(contraseña)

else:
    print ("Error se debe especificar si o no")
    exit(15)