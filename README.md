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

מערכת שמאפשרת למשתמש לעקוב אחרי ההוצאות הכספיות שלו לפי קטגוריות, לראות סיכומים חודשיים, ולהשוות תקציבים.

תכנן את הישויות המרכזיות:

אילו טבלאות יהיו?

אילו שדות צריך בכל טבלה?

מה הקשרים ביניהן (1:1 / 1:N / N:M)?

דוגמה לשאלות:

האם כל הוצאה צריכה תאריך?

איך נרצה לייצג תקציב לקטגוריה מסוימת?

איך תיראה קטגוריה? האם אפשר למחוק אותה? לשתף בין משתמשים?