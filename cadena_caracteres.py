# >>> nombre = input('Cual es tu nombre:')
# Cual es tu nombre:diego
# >>> nombre.upper()
# 'DIEGO'
# >>> nombre.lowcase
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'lowcase'
# >>> nombre.capitalize()
# 'Diego'
# >>> nombre
# 'diego'
# >>> nombre = nombre.capitalize()
# >>> nombre
# 'Diego'
# >>> nombre = nombre.strip()
# >>> nombre
# 'Diego'
# >>> nombre = nombre.lower()
# >>> diego
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'diego' is not defined
# >>> nombre
# 'diego'
# >>> nombre = nombre.replace('o','a')
# >>> nombre
# 'diega'
# >>> nombre [0]
# 'd'
# >>> letra = nombre [2]
# >>> letra
# 'e'
# >>> lent(nombre)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'lent' is not defined
# >>> len(nombre)
# 5
# >>> len(letra)
# 1
# >>> len('Hola! este es el curso de python')
# 32
# >>>

# Slices

# >>> nombre = 'Francisco'
# >>> nombre
# 'Francisco'
# >>> nombre[0:3]
# 'Fra'
# >>> nombre[:3]
# 'Fra'
# >>> nombre[3:]
# 'ncisco'
# >>> nombre[1:7]
# 'rancis'
# >>> nombre[1:7:2]
# 'rni'
# >>> nombre[::-1]
# 'ocsicnarF'
# >>>
# KeyboardInterrupt
# >>>
