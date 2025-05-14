## тест REST API

- **Postman**
- **curl**
- **Python requests**

`curl`:

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

---