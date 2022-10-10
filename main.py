"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""

from prompt_toolkit import prompt


edad= int(prompt("Cuántos años tiene?"))
if edad <= 18 and edad > 0:
    print("Usted es menor de edad")
elif edad < 0:
    print("Numero incorrecto")
else:
    print("usted es mayor de edad")