# Changelog

Wszystkie istotne zmiany w projekcie są dokumentowane w tym pliku.

## [2025-05-24] – Wersja początkowa

### Dodano
- Inicjalizacja repozytorium z podstawową strukturą katalogów (`initial commit`)
- Dodano plik `.gitignore` z wpisami dla PyCharma, macOS i środowiska wirtualnego
- Utworzono `README.md` z opisem projektu i instrukcją uruchamiania
- Dodano `requirements.txt` z zależnościami

## [2025-05-24] – Backend CRUD

### Dodano
- Model `Item` oraz konfiguracja bazy danych
- Funkcje bazowe do tworzenia, pobierania i usuwania rekordów (`crud.py`)
- Endpointy API dla metod `POST`, `GET`, `DELETE` w `main.py`

### Naprawiono
- Błędy importów i brakujący moduł przy uruchamianiu aplikacji
