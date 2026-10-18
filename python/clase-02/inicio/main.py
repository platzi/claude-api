"""Primera llamada real a Claude API con Python."""

import os
from anthropic import Anthropic

MODEL = "claude-sonnet-4-6"


def require_api_key() -> str:
    """Lee la API key desde el entorno para no escribir secretos en código."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("Define ANTHROPIC_API_KEY antes de ejecutar este script.")
    return api_key


def main() -> None:
    client = Anthropic(api_key=require_api_key())
    message = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system="Responde como un mentor breve y práctico de Python.",
        messages=[{"role": "user", "content": "Dame 3 ideas para practicar Claude API."}],
    )

    for block in message.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    main()
