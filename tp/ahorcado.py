#Clone el repo
#Contiene 200 palabras. Si pongo 199 se muestra la última

### IMPORT
import random

### FUNCIONES

def sorteo_palabra (vec):
    palabra = vec[random.randint(0,len(vec)-1)]
    return palabra

def convertir_palabra_a_lista(palabra):
    lista_letra = []
    for letra in palabra:
        lista_letra.append(letra)
    return lista_letra

def buscar_letra(letter, wordList):
    pos_letra_palabra = [False]
    for i in range (len(wordList)):
        if(letter==wordList[i]):
            pos_letra_palabra[0] = True
            pos_letra_palabra.append(i)

    return pos_letra_palabra

def jugar_ahorcado(mensaje_ganador):
    state = 'playing'
    palabra_a_evaluar = sorteo_palabra(['agua'])
    lista_palabra_evaluada = convertir_palabra_a_lista(palabra_a_evaluar)
    palabra_obtenida_jugador = ['_','_','_','_']
    
    while(state == 'playing'):
        letra_a_evaluar = input('Ingrese una letra:')
        lista_posiciones_letra = buscar_letra(letra_a_evaluar,lista_palabra_evaluada)

        if(lista_posiciones_letra[0]==True):
            for pos in range(1,len(lista_posiciones_letra)):
                palabra_obtenida_jugador[lista_posiciones_letra[pos]] = letra_a_evaluar
                print(palabra_obtenida_jugador)
        
        if(palabra_obtenida_jugador == lista_palabra_evaluada):
            state = 'winner'
            print(mensaje_ganador)

### DECLARACION DE VARIABLES

lista_palabras = ["agua", "sol", "casa", "gato", "perro", "libro", "silla", "mesa", "ventana", "puerta", "cielo", "noche", "dia", "rio", "montana", "playa", "mar", "coche", "bicicleta", "flor", "arbol", "nino", "nina", "amigo", "madre", "padre", "hermano", "hermana", "escuela", "parque", "comida", "bebida", "leche", "pan", "fruta", "verdura", "carne", "pescado", "arroz", "pasta", "sopa", "ensalada", "queso", "huevo", "cafe", "te", "jugo", "refresco", "helado", "chocolate", "azucar", "sal", "pimienta", "aceite", "vinagre", "mantequilla", "cuchillo", "tenedor", "cuchara", "plato", "vaso", "taza", "botella", "sarten", "olla", "horno", "microondas", "nevera", "congelador", "lavadora", "secadora", "jabon", "champu", "toalla", "cepillo", "peine", "espejo", "cama", "almohada", "sabana", "manta", "armario", "ropa", "zapato", "calcetin", "pantalon", "camisa", "vestido", "chaqueta", "sombrero", "bufanda", "guante", "anillo", "collar", "reloj", "cinturon", "cartera", "dinero", "moneda", "billete", "banco", "tienda", "mercado", "supermercado", "farmacia", "hospital", "medico", "enfermera", "paciente", "medicina", "pastilla", "inyeccion", "cura", "herida", "fiebre", "tos", "gripe", "virus", "bacteria", "sangre", "hueso", "musculo", "piel", "cerebro", "corazon", "pulmon", "estomago", "higado", "rinon", "intestino", "diente", "ojo", "oreja", "nariz", "boca", "lengua", "labio", "cara", "cabeza", "cuello", "hombro", "brazo", "codo", "muneca", "mano", "dedo", "pierna", "rodilla", "tobillo", "pie", "espalda", "pecho", "vientre", "cadera", "cintura", "gluteo", "frente", "ceja", "pestana", "barba", "bigote", "pelo", "calvo", "alto", "bajo", "gordo", "delgado", "fuerte", "debil", "joven", "viejo", "bebe", "adulto", "hombre", "mujer", "senor", "senora", "chico", "chica", "companero", "vecina", "cliente", "profesor", "alumno", "abuela", "abuelo", "tio", "tia", "primo", "prima", "sobrino", "sobrina", "vecino", "jefe", "colega", "nube", "luna", "estrella", "hoja", "lago"]
palabra_a_evaluar = ''
lista_palabra_evaluada = []
letra_a_evaluar = ''
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