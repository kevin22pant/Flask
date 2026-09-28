"""""
for i in range(5):
    range(5,15),
"""""

def ingresar_lista():
    """Genera una lista de frutas usando range"""
    frutas = ["Manzana", "Plátano", "Naranja", "Uva", "Mango"]

    lista = []
    for i in range(len(frutas)):
        lista.append(frutas[i])
    return lista


if __name__ == "__main__":
    """Ejecuta la función ingresar_lista e imprime sus elementos"""
    mi_lista = ingresar_lista()
    print("\n--- Elementos de la lista ---")
    for i, elemento in enumerate(mi_lista, start=1):
        print(f"{i}. {elemento}")



def ingresar_diccionario():
    """Genera un diccionario de países y sus capitales usando range"""
    paises = [
        ("México", "Ciudad de México"),
        ("España", "Madrid"),
        ("Francia", "París"),
        ("Italia", "Roma"),
        ("Japón", "Tokio")
    ]

    diccionario = {}
    for i in range(len(paises)):
        clave, valor = paises[i]
        diccionario[clave] = valor
    return diccionario


if __name__ == "__main__":
    """Ejecuta la función ingresar_diccionario e imprime sus elementos"""
    mi_diccionario = ingresar_diccionario()
    print("\n--- Elementos del diccionario ---")
    for clave, valor in mi_diccionario.items():
        print(f"{clave}: {valor}")



def imprimir_elementos(lista, diccionario):
    """Imprime los elementos de una lista y un diccionario"""
    print("\n--- Elementos de la lista ---")
    for i, elemento in enumerate(lista, start=1):
        print(f"{i}. {elemento}")

    print("\n--- Elementos del diccionario ---")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    """Genera lista de animales y diccionario de países con capitales usando range"""
    animales = ["Perro", "Gato", "Elefante", "León", "Tigre"]
    mi_lista = [animales[i] for i in range(len(animales))]

    paises = [
        ("Alemania", "Berlín"),
        ("Brasil", "Brasilia"),
        ("Canadá", "Ottawa"),
        ("India", "Nueva Delhi"),
        ("Australia", "Canberra")
    ]
    mi_diccionario = {paises[i][0]: paises[i][1] for i in range(len(paises))}

    """Llama a la función imprimir_elementos para mostrar lista y diccionario"""
    imprimir_elementos(mi_lista, mi_diccionario)



