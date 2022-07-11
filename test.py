from email.utils import parsedate_to_datetime


name = input("\nIntroduce tu nombre: ")
age = input("\nIntroduce tu edad: ")
pasatiempo = input("\nTu pasatiempo favorito: ")

while True:
    print(f"\nHola {name}, es un gusto saludarte!\n")
    print(f"Tu nombre es {name}, tienes {age} años y te gusta jugar {pasatiempo}")
    break