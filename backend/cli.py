"""
cli.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-21
Description:
    Command-line interface (CLI) for interacting with the AI assistant via terminal.
    This script allows users to input questions and receive AI-generated answers in real-time.
"""

# cli.py

from core.ai_config import get_ai_client
from core.assistant import ask_ai
from core.loader import load_all_files
from config.config import SYSTEM_MESSAGES

def main():
    """
    Inicia una sesión de chat en la terminal con el asistente AI.
    Continúa solicitando preguntas hasta que el usuario escriba 'salir', 'exit' o 'quit'.
    """
    client, model = get_ai_client()  # Obtener cliente y modelo
    context = load_all_files()  # Cargar contexto desde los archivos

    # Verifica si el contexto es una cadena de texto y trunca si es necesario
    if not isinstance(context, str):
        context = str(context)  # Asegurarse de que es un string

    # Inicializar la conversación con el mensaje del sistema
    messages = [{"role": "system", "content": SYSTEM_MESSAGES}]

    while True:
        user_question = input("\n¿Qué ayuda necesitas? ")

        if user_question.lower() in ["salir", "exit", "quit"]:
            print("Cerrando sesión. ¡Hasta luego!")
            break

        # Agregar el mensaje del usuario y el contexto truncado
        messages.append({
            "role": "user",
            "content": f"Pregunta: {user_question}\n\nContexto:\n{context[:2000]}"
        })

        # Obtener la respuesta de la IA y agregarla a la conversación
        response = ask_ai(messages)
        messages.append({"role": "assistant", "content": response})

        # Mostrar la respuesta
        print(f"\nRespuesta de {model}:\n")
        print(response)

if __name__ == "__main__":
    main()
