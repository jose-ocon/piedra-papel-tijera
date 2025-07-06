from random import choice
i=0
emp=0
per=0
win=0
mov = ["piedra", "papel", "tijera"]
n=int(input("Ingrese numero de rondas "))
while i<n:
    usuario=input("Elige un movimiento ")
    if usuario in mov:
        pc = choice(mov)
        print("movimiento de la ia", pc)
        if usuario == pc:
            print("Empate")
            emp+=1
        elif usuario == 'piedra' and pc == 'tijera':
            print("Ganaste")
            win+=1
        elif usuario == 'tijera' and pc == 'papel':
            print("Ganaste")
            win+=1
        elif usuario == 'papel' and pc == 'piedra':
            print("Ganaste")
            win+=1
        else:
            print("Perdiste")
            per+=1
        i+=1

if emp>0:
    print("Empataste ", emp, "veces")
print("Ganaste ", win, "veces")
print("Perdiste ", per, "veces")
