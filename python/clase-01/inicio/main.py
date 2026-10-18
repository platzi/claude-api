"""Clase 01 - inicio: Quickstart: tu primera llamada a Claude API.

Este archivo es el punto de partida de la clase. Está lleno de pistas y
TODOs para que el estudiante escriba el código durante la explicación.
"""

import os
from anthropic import Anthropic

MODEL = "claude-sonnet-4-6"

def require_api_key() -> str:
    """Valida que exista ANTHROPIC_API_KEY antes de llamar a la API."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "No se encontró ANTHROPIC_API_KEY. "
            "Exporta la variable de entorno antes de ejecutar el ejemplo."
        )
    return api_key

def main() -> None:
    api_key = require_api_key()
    client = Anthropic(api_key=api_key)
    message  = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system="Responde como un mentor breve y practico de Python.",
        messages=[
            {"role": "user", "content": "Dame 3 ideas de proyectos simples para practicar Claude API"},
        ],
    )

    for block in message.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()
