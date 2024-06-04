#Clone el repo
#Contiene 200 palabras. Si pongo 199 se muestra la última

### IMPORT
import random

### FUNCIONES

def sorteo_palabra (vec):                                                                   # Obtengo una palabra de la lista de palabras
    palabra = vec[random.randint(0,len(vec)-1)]
    return palabra

def convertir_palabra_a_lista(palabra):                                                     # Convierto la palabra a una lista de letras, para poder recorrerla y compararla
    lista_letra = []
    for letra in palabra:
        lista_letra.append(letra)
    return lista_letra

def buscar_letra(letter, wordList):                                                         # Ingreso una letra y lista de letras de la palabra
    pos_letra_palabra = [False]                                                             # Seteo a False para que en caso de que no exista la letra en la palabra, quede en False
    for i in range (len(wordList)):                                                         # Recorro el largo de la lista de letras
        if(letter==wordList[i]):                                                            # Verifico que coincida la letra con la posicion de la lista que toque en esa iteracion
            pos_letra_palabra[0] = True                                                     # Seteo en True el primer campo
            pos_letra_palabra.append(i)                                                     # Me guardo la posicion en la que la letra coincidio

    return pos_letra_palabra           
    
def jugar_ahorcado(mensaje_ganador):
    state = 'playing'                                                                       # Defino la variable con el estado del juego
    palabra_a_evaluar = sorteo_palabra(['agua'])                                            # Obtengo la palabra que voy a tener que adivinar
    lista_palabra_evaluada = convertir_palabra_a_lista(palabra_a_evaluar)                   # Convierto la palabra a una lista de letras, para poder recorrerla
    palabra_obtenida_jugador = ['_','_','_','_']                                            # Genero una lista con espacios vacios iguales a la cantidad de letras de la palabra a adivinar, es la que voy a usar para ir completando la palabra
    VIDAS_TOTAL = 4

    while(state == 'playing'):                                                              # Mientras el estado sea playing, sigo jugando
        letra_a_evaluar = input('Ingrese una letra:')                                       # Solicito al usuario la primer letra
        lista_posiciones_letra = buscar_letra(letra_a_evaluar,lista_palabra_evaluada)       # Utiliza buscar_letra para obtener True/False y las posiciones de las letras

        if(lista_posiciones_letra[0]==True):                                                # Si la primera posicion es True, ejecuto el codigo para completar palabra_obtenida_jugador
            for pos in range(1,len(lista_posiciones_letra)):                                # Recorro la lista de posiciones que tienen la letra, a partir de la posicion 1 porque la 0 tiene el True/False
                palabra_obtenida_jugador[lista_posiciones_letra[pos]] = letra_a_evaluar     # Completa la posicion que tiene la letra con la letra que se esta evaluando
                print(palabra_obtenida_jugador)
        elif lista_posiciones_letra[0]==False:                                              #Si la letra no está dentro de la lista, vidas -1
            VIDAS_TOTAL -=1
            print ("Esa letra no se encuentra. Has perdido una vida. Tu total de vidas es de: ", VIDAS_TOTAL)

        if(palabra_obtenida_jugador == lista_palabra_evaluada):                             # Verifico si mi palabra_obtenida_jugador es igual la que busco adivinar
            print(mensaje_ganador)                                                          # Imprimo en consola el mensaje de ganador
            state = 'winner'                                                                # Cambio el state a winner, para terminar de jugar
        
        if VIDAS_TOTAL == 0:
            state ='lose'
            print  ("¡Has perdido!")

### DECLARACION DE VARIABLES

lista_palabras = ["agua", "sol", "casa", "gato", "perro", "libro", "silla", "mesa", "ventana", "puerta", "cielo", "noche", "dia", "rio", "montana", "playa", "mar", "coche", "bicicleta", "flor", "arbol", "nino", "nina", "amigo", "madre", "padre", "hermano", "hermana", "escuela", "parque", "comida", "bebida", "leche", "pan", "fruta", "verdura", "carne", "pescado", "arroz", "pasta", "sopa", "ensalada", "queso", "huevo", "cafe", "te", "jugo", "refresco", "helado", "chocolate", "azucar", "sal", "pimienta", "aceite", "vinagre", "mantequilla", "cuchillo", "tenedor", "cuchara", "plato", "vaso", "taza", "botella", "sarten", "olla", "horno", "microondas", "nevera", "congelador", "lavadora", "secadora", "jabon", "champu", "toalla", "cepillo", "peine", "espejo", "cama", "almohada", "sabana", "manta", "armario", "ropa", "zapato", "calcetin", "pantalon", "camisa", "vestido", "chaqueta", "sombrero", "bufanda", "guante", "anillo", "collar", "reloj", "cinturon", "cartera", "dinero", "moneda", "billete", "banco", "tienda", "mercado", "supermercado", "farmacia", "hospital", "medico", "enfermera", "paciente", "medicina", "pastilla", "inyeccion", "cura", "herida", "fiebre", "tos", "gripe", "virus", "bacteria", "sangre", "hueso", "musculo", "piel", "cerebro", "corazon", "pulmon", "estomago", "higado", "rinon", "intestino", "diente", "ojo", "oreja", "nariz", "boca", "lengua", "labio", "cara", "cabeza", "cuello", "hombro", "brazo", "codo", "muneca", "mano", "dedo", "pierna", "rodilla", "tobillo", "pie", "espalda", "pecho", "vientre", "cadera", "cintura", "gluteo", "frente", "ceja", "pestana", "barba", "bigote", "pelo", "calvo", "alto", "bajo", "gordo", "delgado", "fuerte", "debil", "joven", "viejo", "bebe", "adulto", "hombre", "mujer", "senor", "senora", "chico", "chica", "companero", "vecina", "cliente", "profesor", "alumno", "abuela", "abuelo", "tio", "tia", "primo", "prima", "sobrino", "sobrina", "vecino", "jefe", "colega", "nube", "luna", "estrella", "hoja", "lago"]
palabra_a_evaluar = ''
mensaje_victoria = 'Ganaste la partida!'



### CODIGO DE EJECUCION
"""
letra_a_evaluar = input('Ingrese una letra:')

palabra_a_evaluar = sorteo_palabra(lista_palabras)
print (palabra_a_evaluar)

lista_palabra_evaluada = convertir_palabra_a_lista(palabra_a_evaluar)
print(lista_palabra_evaluada)

print(buscar_letra(letra_a_evaluar,lista_palabra_evaluada))"""

jugar_ahorcado(mensaje_victoria)