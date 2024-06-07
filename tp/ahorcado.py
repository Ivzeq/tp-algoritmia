#Clone el repo
#Contiene 200 palabras. Si pongo 199 se muestra la última

### IMPORT
import random

### FUNCIONES

# Convierte la palabra a una lista de letras, para poder recorrerla y compararla.
def convertir_palabra_a_lista(palabra):                                                    
    lista_letra = []
    for letra in palabra:
        lista_letra.append(letra)
    return lista_letra

# Sortea la palabra que va a ser adivinada y la devuelve como lista, usamos la función anterior.
def sorteo_palabra (vec):
    sorteo = vec[random.randint(0,len(vec)-1)]
    palabra = convertir_palabra_a_lista(sorteo)
    return palabra

# Busca si la letra ingresada está contenida en la palabra sorteada.
def buscar_letra(letra, palabra):                                                    
    contiene_letra = False                                                             
    for i in range (len(palabra)):                                                         
        if(letra==palabra[i]):                                                             
            contiene_letra = True                                                    
    return contiene_letra

# Genera una lista vacía del mismo tamaño que la palabra sorteada.
def generar_lista(palabra):
    lista = []
    for i in range (len(palabra)):
        lista.append("_")
    return lista

# LLena la lista vacía con las letras que va ingresando el usuario.
def llenar_lista(letra,palabra,lista):
    for i in range (len(palabra)):
        if (letra == palabra[i]):
            lista[i] = letra
    return lista

# Verifica si la letra no fue ingresada previamente.
def letra_repetida(letra):
    letra = letra.lower()
    if letra in letras_ingresadas:
        return True
    else:
        return False         

# Ejecuta el juego.
def jugar_ahorcado(mensaje_ganador):
    state = 'playing'                                                                      # Defino la variable con el estado del juego
    palabra_sorteada = sorteo_palabra(lista_palabras)                                      # Obtengo la palabra que voy a tener que adivinar
    lista_vacia = generar_lista(palabra_sorteada)                                          # Genero una lista con espacios vacios iguales a la cantidad de letras de la palabra a adivinar, es la que voy a usar para ir completando la palabra
    VIDAS_TOTAL = 4                                                                        # Defino la cantidad de vidas en el juego.

    while(state == 'playing'):                                                             # Inicio el ciclo validando que el estado de juego sea 'playing'
        while palabra_sorteada != lista_vacia and VIDAS_TOTAL > 0:                         # Inicio otro ciclo validando que la lista no sea igual que la palabra, de lo contrario la palabra ya habría sido adivinada.
            letra = input("Ingrese una letra: ")                                           # Solicito al usuario ingresar una letra
            if (letra_repetida(letra) == False):                                           # Verifico que la letra no haya sido ingresada anteriormente, de lo contrario no podemos seguir jugando
                if (buscar_letra(letra, palabra_sorteada) == True):                        # Verifico que la letra esté contenida en la palabra sorteada, de lo contrario perdemos una vida
                    print(llenar_lista(letra,palabra_sorteada,lista_vacia))                # Muestro al usuario como queda la lista vacía con la letra ingresada
                    letras_ingresadas.append(letra)                                        # Agrego la letra ingresada en una lista para que no pueda volver a ser utilizada
                else:
                    VIDAS_TOTAL -=1                                                        # Si la letra ingresada no está contenida en la palabra sorteada, descontamos una vida
                    print ("Esa letra no se encuentra. Has perdido una vida. Tu total de vidas es de: ", VIDAS_TOTAL)
            else:
                print("Esa letra ya fue ingresada, intentá nuevamente.")                   # Si la letra ingresada ya fue ingrgesada anteriormente, solicitamos otra letra.
        
        if (palabra_sorteada == lista_vacia):                                              # Verifico que la lista es igual a la palabra sorteada
            print(mensaje_ganador)                                                         # Muestro el mensaje ganador
            state = 'winner'                                                               # Cambio el estado a 'winner' para que el juego termine
        else:
            state ='lose'                                                                  # Cambio el estado a 'lose' para que el juego termine
            print  ("¡Has perdido!")                                                       # Muestro el mensaje perdedor

### DECLARACION DE VARIABLES

lista_palabras = ["agua", "sol", "casa", "gato", "perro", "libro", "silla", "mesa", "ventana", "puerta", 
                  "cielo", "noche", "dia", "rio", "montana", "playa", "mar", "coche", "bicicleta", "flor", 
                  "arbol", "nino", "nina", "amigo", "madre", "padre", "hermano", "hermana", "escuela", "parque",
                  "comida", "bebida", "leche", "pan", "fruta", "verdura", "carne", "pescado", "arroz", "pasta", 
                  "sopa", "ensalada", "queso", "huevo", "cafe", "te", "jugo", "refresco", "helado", "chocolate", 
                  "azucar", "sal", "pimienta", "aceite", "vinagre", "mantequilla", "cuchillo", "tenedor", "cuchara", 
                  "plato", "vaso", "taza", "botella", "sarten", "olla", "horno", "microondas", "nevera", "congelador", 
                  "lavadora", "secadora", "jabon", "champu", "toalla", "cepillo", "peine", "espejo", "cama", "almohada", 
                  "sabana", "manta", "armario", "ropa", "zapato", "calcetin", "pantalon", "camisa", "vestido", "chaqueta", 
                  "sombrero", "bufanda", "guante", "anillo", "collar", "reloj", "cinturon", "cartera", "dinero", "moneda", 
                  "billete", "banco", "tienda", "mercado", "supermercado", "farmacia", "hospital", "medico", "enfermera", 
                  "paciente", "medicina", "pastilla", "inyeccion", "cura", "herida", "fiebre", "tos", "gripe", "virus", 
                  "bacteria", "sangre", "hueso", "musculo", "piel", "cerebro", "corazon", "pulmon", "estomago", "higado", 
                  "rinon", "intestino", "diente", "ojo", "oreja", "nariz", "boca", "lengua", "labio", "cara", "cabeza", 
                  "cuello", "hombro", "brazo", "codo", "muneca", "mano", "dedo", "pierna", "rodilla", "tobillo", "pie", 
                  "espalda", "pecho", "vientre", "cadera", "cintura", "gluteo", "frente", "ceja", "pestana", "barba", 
                  "bigote", "pelo", "calvo", "alto", "bajo", "gordo", "delgado", "fuerte", "debil", "joven", "viejo", 
                  "bebe", "adulto", "hombre", "mujer", "senor", "senora", "chico", "chica", "companero", "vecina", 
                  "cliente", "profesor", "alumno", "abuela", "abuelo", "tio", "tia", "primo", "prima", "sobrino", 
                  "sobrina", "vecino", "jefe", "colega", "nube", "luna", "estrella", "hoja", "lago"]
letras_ingresadas=[]
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