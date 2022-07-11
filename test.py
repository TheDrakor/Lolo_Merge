name = input("\nIntroduce tu nombre: ")
age = input("\nIntroduce tu edad: ")
pasatiempo = input("\nTu pasatiempo favorito: ")

ni = int(input("\nDame un numero de inicio: "))
nf = int(input("Dame un numero para un final: "))

while True:
    print(f"\nHola {name}, es un gusto saludarte!\n")
    print(f"Tu nombre es {name}, tienes {age} años y te gusta jugar {pasatiempo}")
    break
for i in range(ni,nf+1):
    print(i)