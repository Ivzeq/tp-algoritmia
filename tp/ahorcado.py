#Clone el repo
#Contiene 335 palabras. Lo que sería que si imprimo la última. tengo que poner 334 = invierno

def verificaLetra(letter, word):
    posLetraPalabra = [False]
    for i in range (len(word)):
        if(letter==word[i]):
            posLetraPalabra[0] = True
            posLetraPalabra.append(i)

    return posLetraPalabra




vec = ["agua", "sol", "casa", "gato", "perro", "libro", "silla", "mesa", "ventana", "puerta", "cielo", "noche", "día", "río", "montaña", "playa", "mar", "coche", "bicicleta", "flor", "árbol", "niño", "niña", "amigo", "madre", "padre", "hermano", "hermana", "escuela", "parque", "comida", "bebida", "leche", "pan", "fruta", "verdura", "carne", "pescado", "arroz", "pasta", "sopa", "ensalada", "queso", "huevo", "café", "té", "jugo", "refresco", "helado", "chocolate", "azúcar", "sal", "pimienta", "aceite", "vinagre", "mantequilla", "cuchillo", "tenedor", "cuchara", "plato", "vaso", "taza", "botella", "sartén", "olla", "horno", "microondas", "nevera", "congelador", "lavadora", "secadora", "jabón", "champú", "toalla", "cepillo", "peine", "espejo", "cama", "almohada", "sábana", "manta", "armario", "ropa", "zapato", "calcetín", "pantalón", "camisa", "vestido", "chaqueta", "sombrero", "bufanda", "guante", "anillo", "collar", "reloj", "cinturón", "cartera", "dinero", "moneda", "billete", "banco", "tienda", "mercado", "supermercado", "farmacia", "hospital", "médico", "enfermera", "paciente", "medicina", "pastilla", "inyección", "cura", "herida", "fiebre", "tos", "gripe", "virus", "bacteria", "sangre", "hueso", "músculo", "piel", "cerebro", "corazón", "pulmón", "estómago", "hígado", "riñón", "intestino", "diente", "ojo", "oreja", "nariz", "boca", "lengua", "labio", "cara", "cabeza", "cuello", "hombro", "brazo", "codo", "muñeca", "mano", "dedo", "pierna", "rodilla", "tobillo", "pie", "espalda", "pecho", "vientre", "cadera", "cintura", "glúteo", "frente", "ceja", "pestaña", "barba", "bigote", "pelo", "calvo", "alto", "bajo", "gordo", "delgado", "fuerte", "débil", "joven", "viejo", "bebé", "adulto", "hombre", "mujer", "señor", "señora", "chico", "chica", "compañero", "vecina", "cliente", "profesor", "alumno", "abuela", "abuelo", "tío", "tía", "primo", "prima", "sobrino", "sobrina", "bebé", "vecino", "jefe", "colega", "nube", "luna", "estrella", "hoja", "lago", "tren", "avión", "barco", "pelota", "muñeca", "juguete", "revista", "teléfono", "radio", "televisión", "película", "canción", "piano", "guitarra", "tambor", "violín", "voz", "lengua", "nube", "árbol", "flor", "pez", "pájaro", "ratón", "león", "tigre", "oso", "mono", "elefante", "jirafa", "caballo", "vaca", "cerdo", "oveja", "cabra", "gallina", "pato", "pavo", "ángel", "fantasma", "dragón", "unicornio", "ogro", "duende", "elfo", "hada", "brujo", "hechicero", "varita", "pócima", "magia", "espada", "escudo", "arco", "flecha", "lanza", "casco", "armadura", "castillo", "torre", "muralla", "escalera", "lámpara", "pluma", "tinta", "papel", "pergamino", "joya", "pulsera", "corona", "trono", "cetro", "tapiz", "bandera", "mapa", "brújula", "campana", "baile", "fiesta", "banquete", "pan", "pastel", "dulce", "miel", "especia", "planta", "raíz", "fruto", "lluvia", "hielo", "trueno", "tormenta", "estrella", "planeta", "meteoro", "galaxia", "universo", "espacio", "pasado", "presente", "futuro", "mañana", "tarde", "hora", "minuto", "segundo", "calendario", "fecha", "año", "mes", "semana", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", "primavera", "verano", "otoño", "invierno"]
print (vec[334])
palabraEvaluada = ['a','g','u','a']

print(verificaLetra('a',palabraEvaluada))