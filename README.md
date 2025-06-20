activate venv:

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\venv\Scripts\Activate.ps1


run server:

uvicorn app.main:app --reload

Swagger UI: http://127.0.0.1:8000/docs

docker commands:

docker compose build
docker ps -a
docker compose up -d
docker compose down      
docker compose down -v
docker logs -f

postgres:
mydatabase
postgres
postgres

pgadmin
admin@admin.com
admin
http://localhost:5050