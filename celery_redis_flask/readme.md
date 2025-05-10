Запуск:

1. **redis**
   ```bash
   redis-server
   ```

2. зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. **celery** worker:
   ```bash
   celery -A tasks.celery_app worker --loglevel=info
   ```

4. **flask**-приложение:
   ```bash
   python app.py
   ```

5. тест:

**POST /submit**
```json
{
  "n": 10000
}
```

**GET /result/{task_id}**

---
- Postman 
- curl 
- Python requests
curl
```bash
# Получить все задачи
curl http://localhost:5000/tasks

# Создать новую задачу
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Изучить Celery"}'

# Получить задачу с ID=1
curl http://localhost:5000/tasks/1

# Обновить задачу
curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"status": "completed"}'

# Удалить задачу
curl -X DELETE http://localhost:5000/tasks/1
```

Что показывает данный проект обо мне?

Я могу:
 - Сделать веб-приложение, работающее с мобильными или - десктопными клиентами.
 - Позволить другим сервисам общаться с приложением.
 - Разделить фронтенд и бэкенд (например, фронтенд фреймворк + Flask).
 - Создать внутренний API для микросервисной архитектуры.
 - Реализовать CRUD-интерфейс для управления задачами.
     