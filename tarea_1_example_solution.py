# ==================================
# EJERCICIO 1
# ==================================


"""El metodo cambio recibe como unico parametro
una variable de tipo String,
esta pensada para recibir un caracter
dentro de el alfabeto, como salida devuelve el mismo
 caracter pero en su mayuscula o minuscula dependiendo del
valor recibido. A traves de una serie de condicionales si el
 caracter recibido es una letra en mayuscula se retorna
la misma letra pero en minuscula y viceversa.
Ademas si el parametro que se le da a la funcion
esta fuera del abecedario entonces retorna un None """


def cambio(letra):
    if letra == "a":
        return ("A")
    elif letra == "A":
        return ("a")
    elif letra == "b":
        return ("B")
    elif letra == "B":
        return ("b")
    elif letra == "c":
        return ("C")
    elif letra == "C":
        return ("c")
    elif letra == "d":
        return ("D")
    elif letra == "D":
        return ("d")
    elif letra == "e":
        return ("E")
    elif letra == "E":
        return "e"
    elif letra == "f":
        return ("F")
    elif letra == "F":
        return ("f")
    elif letra == "g":
        return ("G")
    elif letra == "G":
        return ("g")
    elif letra == "h":
        return ("H")
    elif letra == "H":
        return ("h")
    elif letra == "i":
        return ("I")
    elif letra == "I":
        return ("i")
    elif letra == "j":
        return ("J")
    elif letra == "J":
        return ("j")
    elif letra == "k":
        return ("K")
    elif letra == "K":
        return ("k")
    elif letra == "l":
        return ("L")
    elif letra == "L":
        return ("l")
    elif letra == "m":
        return ("M")
    elif letra == "M":
        return ("m")
    elif letra == "n":
        return ("N")
    elif letra == "N":
        return ("n")
    elif letra == "o":
        return ("O")
    elif letra == "O":
        return ("o")
    elif letra == "p":
        return ("P")
    elif letra == "P":
        return ("p")
    elif letra == "q":
        return ("Q")
    elif letra == "Q":
        return ("q")
    elif letra == "r":
        return ("R")
    elif letra == "R":
        return ("r")
    elif letra == "s":
        return ("S")
    elif letra == "S":
        return ("s")
    elif letra == "t":
        return ("T")
    elif letra == "T":
        return ("t")
    elif letra == "u":
        return ("U")
    elif letra == "U":
        return ("u")
    elif letra == "v":
        return ("V")
    elif letra == "V":
        return ("v")
    elif letra == "w":
        return ("W")
    elif letra == "W":
        return ("w")
    elif letra == "x":
        return ("X")
    elif letra == "X":
        return ("x")
    elif letra == "y":
        return ("Y")
    elif letra == "Y":
        return ("y")
    elif letra == "z":
        return ("Z")
    elif letra == "Z":
        return ("z")
    elif letra == " ":
        return (" ")
    else:
        return None


"""El metodo invert_case recibe un unico parametro correspondiente a una
cadena de caracteres String y retorna como salida la misma cadena
pero con las mayusculas y minusculas invertidas, sin embargo esta
entrada restricciones requeridas por el solicitante"""


def invert_case(Cadena):

    # Se verifica si el caracter proveido es de tipo String
    if not isinstance(Cadena, str):
        return (-16, None)
    # Se verifica que Cadena no sea un string vacio
    if not Cadena.strip():
        return (-48, None)
    nueva = ""  # Variable que almacenara la cadena de caracteres invertidos
    """El primer bucle for se encarga de recorrer la cadena de caracteres,
    con ayuda de la funcion cambio detecta si hay un caracter no perteneciente
    al abecedario en caso de haberlo retorna un none"""
    for i in Cadena:
        x = cambio(i)  # Se almacena cada caracter invertido para concaternarlo
        if x is None:
            return (-32, None)
        nueva = nueva+x

    return (0, nueva)
# ================================================
# EJERCICIO 2
# ================================================


""" El metodo esprimo funciona como una funcion complementaria,
cummple la funcion de determinar si un numero es o no primo,
recibe un numero entero como entrada y devuelve un valor booleano,
 True si el numero es primo y false si no"""


def esprimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


"""  El metodo numero_primo es el metodo solicitado, usa como complemente a
la funcion esprimo y recibe como entrada un solo numero
y devuelve una lista con todos los numeros primo desde el 1 hasta el mismo """


def numero_primo(base):
    # se procede a realizar las restricciones solicitadas en el enunciado
    if base == 0:
        return 0, []
    elif base is True:
        return -64, None
    elif base is False:
        return -64, None
    elif not isinstance(base, int):
        return -64, None
    elif base > 100:
        return -80, None
    numeros = []    # Variable en la que se almacenaran los numero a retornar
    """Se recorre en un bucle todos los numeros uno a uno hasta llegar
      a la base.
      En el proceso se discriminan los primos y se agregan a una lista """
    for i in range(base+1):
        if esprimo(i) is True:
            numeros.append(i)
    return (0, numeros)
