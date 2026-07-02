# Repozytorium Bazowe

To repozytorium zawiera podstawową konfigurację startową:
- `.gitignore` dla typowych plików lokalnych i cache narzędzi.
- `Dockerfile` do uruchamiania środowiska roboczego w kontenerze.
- `.dockerignore` ograniczający kontekst buildu obrazu.

## Uruchomienie kontenera

Zbuduj obraz:

```bash
docker build -t codex-workspace .
```

Uruchom kontener:

```bash
docker run --rm -it -v "$(pwd):/workspace" codex-workspace
```

## Klonowanie zewnętrznego repozytorium (opcjonalnie)

Jeśli chcesz zainicjalizować to repozytorium zawartością projektu `langchain-ai/langchain`,
wykonaj lokalnie (poza tym środowiskiem):

```bash
gh repo clone langchain-ai/langchain .
```
