def responder(mensaje):
    mensaje = mensaje.lower()

    if "hola" in mensaje:
        return "Hola, ¿cómo estás?"
    elif "adios" in mensaje:
        return "Hasta luego"
    else:
        return "No entiendo"

def main():
    while True:
        texto = input(">> ")
        if texto == "salir":
            break
        print(responder(texto))

if __name__ == "__main__":
    main()