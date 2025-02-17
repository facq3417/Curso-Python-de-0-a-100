# 1.- Comentario de una sola linea (#)
# Se escriben con el símbolo # y solo afectan la línea en la que se encuentran

x = 10 
print(x)

# 2.- Comentarios de múltiples líneas (''' o """)
# Para escribir comentarios en varias líneas, usamos comillas triples (''' o """).

"""
Este es un comentario 
de varias líneas en Python.
Sirve para documentar funciones y código.
"""

print("Hola, Python")

# También se puede usar con comillas simples:

'''
Otro comentario
de múltiples líneas.
'''
print("Aprendiendo Python")


# Nota: Aunque las comillas triples se usan para comentarios largos, 
# técnicamente Python las trata como cadenas de texto (strings) sin asignar a una variable.

# 3. Docstrings (""" dentro de funciones o clases)

#Los docstrings documentan funciones, métodos o clases y se colocan en la primera línea dentro de ellas.

def suma(a, b):
    """Esta función recibe dos números y devuelve su suma."""
    return a + b

print(suma.__doc__)  # Muestra la documentación de la función



#Diferencia entre Docstrings y Comentarios:
#Los comentarios (#) son ignorados completamente por Python.
#Los docstrings (""") quedan almacenados y se pueden acceder con .__doc__.

