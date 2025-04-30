"""
cli.py

Author: Edgar Masagué (https://github.com/edgarmasague)
Created: 2025-04-25
Version: 1.0.0
License: MIT
Description:
    Command-line interface (CLI) for interacting with the AI assistant via terminal.
    This script allows users to input questions and receive AI-generated answers in real-time.
"""
from core.assistant import process_message_flow
from core.i18n import get_translation
from config.config import SYSTEM_MESSAGES


def select_lang():
    print("\nSelect 1 to English")
    print("\nSelecciona 2 para Español")
    print("\nSelecione 3 para Português")
    while True:
        choice = input("Opción (1/2/3): ").strip()
        if choice in ["1", "2", "3"]:
            return {
                "1": "en",
                "2": "es",
                "3": "pt"
            }[choice]
        print("Error: 1, 2 o 3.")

def main():
    lang = select_lang()
    t = get_translation(lang)
    
    print(t["welcome"])
    
    while True:
        try:
            user_input = input(f"{t['prompt']} ")
            
            if not user_input.strip():
                print(t["empty_warning"])
                continue
                
            if user_input.lower() in t["exit_commands"]:
                print(t["goodbye"])
                break

            response = process_message_flow(
                user_message=user_input,
                system_prompt=SYSTEM_MESSAGES,
                session_id="cli-session"
            )
            
            print(f"🤖 {response}")

        except KeyboardInterrupt:
            print("\n" + t["goodbye"])
            break
        except Exception as e:
            print(f"🔥 {t['error']}: {str(e)}")

if __name__ == "__main__":
    main()