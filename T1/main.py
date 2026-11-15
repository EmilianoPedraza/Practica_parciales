import random
from clase import Incursion

def add_in_order(v, pk):
    n,pos = (len(v) - 1), 0
    izq, der = 0, n
    while izq <= der:
        centro = (izq + der) // 2
        if v[centro].nombre == pk.nombre:
            pos = centro
            break
        if v[centro].nombre > pk.nombre:
            der = centro - 1
        else:
            izq = centro + 1
    if izq > der:
        pos = izq
    v[pos:pos]= [pk]

def generar_aleatorio():
    NOMBRES = (
        "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon",
        "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie",
        "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill",
        "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate",
        "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu",
        "Sandshrew", "Sandslash", "Nidorino", "Nidorina", "Nidoqueen",
        "Nidorina", "Nidorino", "Nidoking", "Clefairy", "Clefable",
        "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat",
        "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect"
    )
    nombre = random.choice(NOMBRES)
    gimnasio = random.randint(1, 3)
    nivel = random.randint(1, 5)
    tipo = random.randint(1, 3)
    forma = random.randint(1, 2)
    cantidad = random.randint(5, 10)
    adicionales = random.randint(0, 20)
    return Incursion(nombre, gimnasio, nivel, tipo, forma, cantidad, adicionales)

# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))

def valid(msj):
    while True:
        n = int(input(msj))
        if n > 0:
            return n
        print('Error... ingrese valor valido')


def options():
    print('')


