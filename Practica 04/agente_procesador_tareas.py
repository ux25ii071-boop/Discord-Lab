import tareas_agente


def ejecutar_comando(comando: str):
    comando = comando.lower().strip()

    if comando == "ayuda":
        return tareas_agente.mostrar_ayuda()

    elif comando == "crear":
        return tareas_agente.crear_tarea()

    elif comando == "listar":
        return tareas_agente.listar_tareas()

    elif comando.startswith("agregar"):
        tarea = comando.replace("agregar", "").strip()
        return tareas_agente.agregar_tarea(tarea)

    elif comando.startswith("eliminar"):
        tarea = comando.replace("eliminar", "").strip()
        return tareas_agente.eliminar_tarea(tarea)

    elif comando == "estado":
        return tareas_agente.estado()

    else:
        return "Comando no reconocido. Usa !ayuda"