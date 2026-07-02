# Repozytorium Bazowe

To repozytorium zawiera podstawową konfigurację startową wraz z połączeniem do OpenAI ChatGPT API:
- `.gitignore` dla typowych plików lokalnych, cache narzędzi i pliku `.env`.
- `.env.example` — szablon zmiennych środowiskowych (skopiuj jako `.env` i uzupełnij klucz API).
- `Dockerfile` do uruchamiania środowiska roboczego w kontenerze.
- `.dockerignore` ograniczający kontekst buildu obrazu.
- `requirements.txt` z zależnościami (`openai`, `python-dotenv`).
- `chat.py` — prosty klient ChatGPT w trybie konwersacji.

## Konfiguracja klucza API OpenAI

1. Skopiuj plik przykładowy:
   ```bash
   cp .env.example .env
   ```
2. Otwórz `.env` i wstaw swój klucz API:
   ```
   OPENAI_API_KEY=sk-...twój_prawdziwy_klucz...
   ```
   Klucz możesz wygenerować na stronie: https://platform.openai.com/api-keys

> **Uwaga:** plik `.env` jest dodany do `.gitignore` — nie zostanie przypadkowo opublikowany w repozytorium.

## Uruchomienie czatu (lokalnie)

```bash
pip install -r requirements.txt
python chat.py
```

## Uruchomienie kontenera

Zbuduj obraz:

```bash
docker build -t codex-workspace .
```

Uruchom kontener przekazując plik `.env`:

```bash
docker run --rm -it --env-file .env -v "$(pwd):/workspace" codex-workspace
```

Następnie w kontenerze:

```bash
python chat.py
```

## Klonowanie zewnętrznego repozytorium (opcjonalnie)

Jeśli chcesz zainicjalizować to repozytorium zawartością projektu `langchain-ai/langchain`,
wykonaj lokalnie (poza tym środowiskiem):

```bash
gh repo clone langchain-ai/langchain .
```
