from random import*

#input
print("--------------------- Piedra Papel o Tigeras ----------------------------")
usuario = int(input("seleccione una opcion : 1(piedra) 2(papel) 3(tijeras) : "))

#variables
maquina = randint(1,3)
puntuacion1 = 0
puntuacion2 = 0

#procesing
if usuario == 1:
    if maquina == 1:
        RTA = "Empate"
    elif maquina == 2:
        RTA = "Perdiste"
        puntuacion2 += 1
    elif maquina == 3:
        RTA = "Ganaste"
        puntuacion1 += 1
elif usuario == 2:
    if maquina == 2:
        RTA = "Empate"
    elif maquina == 3:
        RTA = "Perdiste"
        puntuacion2 += 1
    elif maquina == 1:
        RTA = "Ganaste"
        puntuacion1 += 1
elif usuario == 3:
    if maquina == 3:
        RTA = "Empate"
    elif maquina == 1:
        RTA = "Perdiste"
        puntuacion2 += 1
    elif maquina == 2:
        RTA = "Ganaste"
        puntuacion1 += 1

if usuario == 1:
    resultado1 = "Piedra"
elif usuario == 2:
    resultado1 = "papel"
elif usuario == 3:
    resultado1 = "tijera"

if maquina == 1:
    resultado2 = "Piedra"
elif maquina == 2:
    resultado2 = "papel"
elif maquina == 3:
    resultado2 = "tijera"


print("--------------------- Resultados -----------------------------------------")
print("tu eleccion fue : ",resultado1)
print("la eleccion de la maquina fue : ",resultado2)
print("------------")
print(RTA)
print("--------- Puntuacion ------------")
print("tu puntacion es : ",puntuacion1)
print("la puntuacion de la maquina es : ",puntuacion2)