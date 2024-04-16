# Métodos de strings

animal = " chanCHito feliz "

# Método upper: transforma el texto del string en mayusculas
print(animal.upper())

# Método lower: transforma el texto del string en minusculas
print(animal.lower())

# Método capitalize: transforma la primera letra del string en mayuscula y el resto en minusculas
# Se incorpopra el método strip para eliminar el primer espacio del string para que capitalize reconozca C como primer caracter.
print(animal.strip().capitalize())

# Método title: transforma la primera letra de cada palabra del string en mayuscula y el resto de letras en minusculas
print(animal.title())

# Método strip: Elimina los espacios en blanco del string a su derecha e izquierda.
print(animal.strip())

# Método lstrip y rstrip: El primero elimina espacios en la izquierda y el segundo elimina espacios en la derecha
print(animal.lstrip())
print(animal.rstrip())

# Método find: busca una cadena de caracteres que le indiquemos en el argumento y si no lo enfuentra nos devuelve el índice
# Si nos devuelve un número positivo significa que encontró el índice que estábamos buscando, pero si nos devuelve -1 significa que no existe
print(animal.find("cH"))

# Método replace: sirve para remplazar caracteres
print(animal.replace("nCH", "j"))

# Verificar que una cadena de caracteres exista en un string
print("nCH" in animal)
print("nCH" not in animal)
