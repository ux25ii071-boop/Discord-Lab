import datetime


def mostrar_ayuda():
    return (
        "Comandos disponibles:\n"
        "1. !definir <termino> - Busca conceptos de Python.\n"
        "2. !validar <nombre> - Revisa si un nombre de variable es válido.\n"
        "3. !hora - Muestra la hora del sistema.\n"
        "4. !ayuda - Muestra esta ayuda."
    )


def analizar_comando(entrada_usuario):
    """
    Segunda fase del Agente: Procesamiento de comandos y lógica dinámica.
    """

    mensaje = entrada_usuario.lower().strip()

    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)

        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None


        if comando == "!definir":
            return buscar_en_diccionario(argumento)


        elif comando == "!validar":
            return validar_variable(argumento)


        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f"La hora actual del servidor es: {ahora}"


        elif comando == "!ayuda":
            return mostrar_ayuda()


        else:
            return f"El comando '{comando}' no existe. Usa '!ayuda'."

    return "Recuerda usar el prefijo '!' para darme órdenes."


def buscar_en_diccionario(termino):

    if not termino:
        return "Debes escribir qué término quieres definir. Ejemplo: !definir lista"


    conocimiento = {
        "variable": "Un espacio en memoria para almacenar datos.",
        "lista": "Colección mutable de elementos.",
        "tupla": "Colección inmutable de elementos."
    }


    return conocimiento.get(
        termino,
        f"No encontré '{termino}' en mi base de datos."
    )


def validar_variable(nombre):

    if not nombre:
        return "Indica el nombre a validar. Ejemplo: !validar mi_variable"


    if nombre[0].isdigit():
        return f"'{nombre}' no es válido: no puede empezar con un número."


    if " " in nombre:
        return f"'{nombre}' no es válido: no puede contener espacios."


    if not nombre.isidentifier():
        return f"'{nombre}' contiene caracteres no permitidos."


    return f"'{nombre}' es un nombre de variable válido en Python."