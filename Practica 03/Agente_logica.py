def analizar(mensaje):
    claves = ["if", "for", "while"]

    for c in claves:
        if c in mensaje.lower():
            return f"Detectado: {c}"

    return "No hay coincidencias"

def main():
    texto = input("Pregunta: ")
    print(analizar(texto))

if __name__ == "__main__":
    main()