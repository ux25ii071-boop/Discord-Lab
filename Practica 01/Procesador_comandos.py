import datetime

def obtener_saludo(nombre_bot):
   """
   retorna un saludo formateado
   """
   return f"Hola, soy  {nombre_bot} y estoy para ayudarte"


def procesar_comando_recordar(comando):
    """
    valida y procesa la accion de recordar un dato

    """
    if not comando:
        return"Error: Falta el nombre. Uso !recordar [nombre]"
    
    return f"¡Entiendo! recordare el nombre: {comando}"


def calcular_uptime(hora_inicio):
    """
    Calcula la diferencia de tiempo entre el inicio
    y el actual (mostrar actividad del bot)
    """

    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"tiempo de actividad: {segundos} segundos"



def mostar_ayuda():
    """"
    comandos disponibles para el usuario
    """

    return (
        "Comandos disponibles \n"
        "!saludo - Muestra un saludo del bot \n"
        "!recordar [nombre] - El bot recordará el nombre proporcionado \n"
        "!uptime - Muestra el timepo de actividad del bot\n"
        "!ayuda - Muestra esta lista de comandos"


    )

#funcion principal para probar las funciones 


def iniciar_agente():
   NOMBRE_BOT = "DiscordYets"
   PREFIJO = "!"
   hora_inicio = datetime.datetime.now()


   print (f"{obtener_saludo(NOMBRE_BOT)}")
   print("Escribe !ayuda para ver los comandos disponibles.")

   ejecutando = True 
   while ejecutando:
       entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()

       if not entrada.startswith(PREFIJO):
           print("Comando desconocido")
           continue
       

       partes = entrada[len(PREFIJO):].split(maxsplit=1)
       comando = partes[0].lower()
       argumento = partes[1] if len(partes) > 1 else ""   

       if comando == "saludo":
           print(obtener_saludo[NOMBRE_BOT])
       elif comando == "ayuda":
           print(mostar_ayuda())

       else:
           print("Comando no reconocido")

def main():
    iniciar_agente()

if __name__ == "__main__":
    main()