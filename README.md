# FastAPI CRUD Example
Przykładowy projekt demonstrujący operacje CRUD (Create, Read, Update, Delete) z użyciem frameworka FastAPI oraz bazy danych PostgreSQL. Projekt został przygotowany w ramach przedmiotu *Narzędzia do automatyzacji budowy oprogramowania*.


## Funkcjonalności
- Endpoint `GET /items/` zwracający wszystkie rekordy z bazy danych
- Endpoint `POST /items/` umożliwiający dodawanie nowych rekordów
- Endpoint `GET /items/{id}` do zwracania rekordów po ID
- Endpoint `PUT /items/{id}` do edycji rekordów po ID
- Endpoint `DELETE /items/{id}` do usuwania rekordów po ID
- Endpoint `POST /persons/` umożliwiający dodawanie nowych osób

## Instalacja
```bash
# Klonowanie repozytorium
git clone https://github.com/spirteque/my-crud-project.git

# Przejście do katalogu projektu
cd my-crud-project

# Tworzenie i aktywacja środowiska wirtualnego
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instalacja zależności
pip install -r requirements.txt
```

## Użycie
```bash
# Uruchomienie aplikacji FastAPI
uvicorn app.main:app --reload

# Po uruchomieniu przejdź do: http://localhost:8000/docs
# Dokumentacja interfejsu API generowana jest automatycznie.
```

## Dokumentacja
Pełna dokumentacja endpointów znajduje się pod /docs w aplikacji FastAPI.


## Licencja
Ten projekt jest licencjonowany pod [licencją MIT](
https://pl.wikipedia.org/wiki/Licencja_MIT).

## Autorzy
- Sylwia – [GitHub](https://github.com/spirteque)

## Podziękowania
- Podziękowania dla twórców FastAPI, SQLModel i społeczności open source


### Inne ważne pliki dokumentacyjne
1. **LICENSE** - plik zawierający pełną treść licencji
2. **CONTRIBUTING.md** - wytyczne dla osób chcących współtworzyć
projekt
3. **CHANGELOG.md** - historia zmian w projekcie
4. **CODE_OF_CONDUCT.md** - zasady zachowania dla społeczności
projektu
5. **.github/ISSUE_TEMPLATE/** - szablony dla zgłaszanych problemów
6. **.github/PULL_REQUEST_TEMPLATE.md** - szablon dla pull requestów

