from datetime import datetime


def obtener_saludo(nombre_bot):
    return f"Hola, soy {nombre_bot}. ¿En qué puedo ayudarte?"


def procesar_comando_recordar(argumento):
    return f"Recordaré: {argumento}"


def calcular_uptime(hora_inicio):
    ahora = datetime.now()
    diferencia = ahora - hora_inicio
    return f"Tiempo activo: {diferencia}"


def mostrar_ayuda():
    return """
Comandos disponibles:
- saludo
- recordar <mensaje>
- uptime
- ayuda
- salir
"""


def iniciar_agente():
    nombre_bot = "AgenteBot"
    hora_inicio = datetime.now()

    print(obtener_saludo(nombre_bot))

    while True:
        comando = input(">> ").strip()

        if comando == "salir":
            print("Apagando agente...")
            break

        elif comando == "saludo":
            print(obtener_saludo(nombre_bot))

        elif comando.startswith("recordar"):
            argumento = comando.replace("recordar", "").strip()
            print(procesar_comando_recordar(argumento))

        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))

        elif comando == "ayuda":
            print(mostrar_ayuda())

        else:
            print("Comando no reconocido. Escribe 'ayuda'.")


def main():
    iniciar_agente()


if __name__ == "__main__":
    main()