# Prosta aplikacja do zadań (Flask)

Prosty skrypt w Pythonie. Udostępnia REST API do listy zadań i zapisuje dane do `tasks.json` w tym samym folderze co skrypt.
To jest moja pierwsza aplikacja Flaskowa
## Funkcje
- dodawanie, pobieranie, aktualizacja i usuwanie zadań
- zapis danych do pliku `tasks.json`
- sensowne kody HTTP (`201`, `404`)
- zero konfiguracji, bez bazy danych

## Wymagania
Python 3.x  
Pakiety: `Flask`

## Instalacja pakietów
```bash
pip install Flask

## Dodawanie
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Kupić mleko"}'

## Aktualizacja
curl -X PUT http://127.0.0.1:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'

## Pobranie
curl http://127.0.0.1:5000/tasks

## Usunięcie
curl -X DELETE http://127.0.0.1:5000/tasks/1