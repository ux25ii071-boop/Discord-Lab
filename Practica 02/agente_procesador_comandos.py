import procesador_comandos


def ejecutar_comando(comando: str):
    comando = comando.lower().strip()

    # comandos simples
    if comando == "ayuda":
        return procesador_comandos.mostrar_ayuda()

    elif comando == "saludo":
        return procesador_comandos.obtener_saludo("PyBot_V2")

    elif comando == "tiempo":
        # como tu función necesita hora_inicio, aquí lo simplificamos
        return "Este comando requiere ejecución dentro del agente principal."

    elif comando.startswith("recordar"):
        argumento = comando.replace("recordar", "").strip()
        return procesador_comandos.procesar_comando_recordar(argumento)

    elif comando == "salir":
        return "Salir"

    else:
        return f"Comando '{comando}' no reconocido. Usa !ayuda."