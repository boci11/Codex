"""
Prosty klient ChatGPT korzystający z OpenAI API.

Użycie:
    python chat.py

Wymagania:
    - Plik .env z ustawionym OPENAI_API_KEY (patrz .env.example)
    - Zainstalowane zależności: pip install -r requirements.txt
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "Brak klucza API. Ustaw OPENAI_API_KEY w pliku .env (patrz .env.example)."
    )

client = OpenAI(api_key=api_key)


def chat(message: str, model: str = "gpt-4o-mini") -> str:
    """Wyślij wiadomość do ChatGPT i zwróć odpowiedź."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    if not response.choices or response.choices[0].message.content is None:
        raise ValueError("API zwróciło pustą odpowiedź.")
    return response.choices[0].message.content


def main() -> None:
    print("Połączono z ChatGPT. Wpisz 'wyjście' aby zakończyć.\n")
    while True:
        user_input = input("Ty: ").strip()
        if user_input.lower() in {"wyjście", "exit", "quit"}:
            print("Do widzenia!")
            break
        if not user_input:
            continue
        try:
            reply = chat(user_input)
        except Exception as exc:
            print(f"Błąd API: {exc}\n")
            continue
        print(f"ChatGPT: {reply}\n")


if __name__ == "__main__":
    main()
