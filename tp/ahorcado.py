#Clone el repo
#Contiene 200 palabras. Si pongo 199 se muestra la última

### IMPORT
import random

def sorteo_palabra (vec):
    palabra = vec[random.randint(0,199)]
    return palabra

###
vec = ["agua", "sol", "casa", "gato", "perro", "libro", "silla", "mesa", "ventana", "puerta", "cielo", "noche", "dia", "rio", "montana", "playa", "mar", "coche", "bicicleta", "flor", "arbol", "nino", "nina", "amigo", "madre", "padre", "hermano", "hermana", "escuela", "parque", "comida", "bebida", "leche", "pan", "fruta", "verdura", "carne", "pescado", "arroz", "pasta", "sopa", "ensalada", "queso", "huevo", "cafe", "te", "jugo", "refresco", "helado", "chocolate", "azucar", "sal", "pimienta", "aceite", "vinagre", "mantequilla", "cuchillo", "tenedor", "cuchara", "plato", "vaso", "taza", "botella", "sarten", "olla", "horno", "microondas", "nevera", "congelador", "lavadora", "secadora", "jabon", "champu", "toalla", "cepillo", "peine", "espejo", "cama", "almohada", "sabana", "manta", "armario", "ropa", "zapato", "calcetin", "pantalon", "camisa", "vestido", "chaqueta", "sombrero", "bufanda", "guante", "anillo", "collar", "reloj", "cinturon", "cartera", "dinero", "moneda", "billete", "banco", "tienda", "mercado", "supermercado", "farmacia", "hospital", "medico", "enfermera", "paciente", "medicina", "pastilla", "inyeccion", "cura", "herida", "fiebre", "tos", "gripe", "virus", "bacteria", "sangre", "hueso", "musculo", "piel", "cerebro", "corazon", "pulmon", "estomago", "higado", "rinon", "intestino", "diente", "ojo", "oreja", "nariz", "boca", "lengua", "labio", "cara", "cabeza", "cuello", "hombro", "brazo", "codo", "muneca", "mano", "dedo", "pierna", "rodilla", "tobillo", "pie", "espalda", "pecho", "vientre", "cadera", "cintura", "gluteo", "frente", "ceja", "pestana", "barba", "bigote", "pelo", "calvo", "alto", "bajo", "gordo", "delgado", "fuerte", "debil", "joven", "viejo", "bebe", "adulto", "hombre", "mujer", "senor", "senora", "chico", "chica", "companero", "vecina", "cliente", "profesor", "alumno", "abuela", "abuelo", "tio", "tia", "primo", "prima", "sobrino", "sobrina", "vecino", "jefe", "colega", "nube", "luna", "estrella", "hoja", "lago"]
print (sorteo_palabra(vec))
