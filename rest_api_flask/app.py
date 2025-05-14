from flask import Flask, jsonify, request

app = Flask(__name__)

# Хранилище задач (в памяти)
tasks = [
    {"id": 1, "title": "Посмотреть лекцию", "status": "pending"},
    {"id": 2, "title": "Сделать домашку", "status": "in progress"}
]

# GET /tasks — получить все задачи
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# GET /tasks/<id> — получить конкретную задачу
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

# POST /tasks — добавить новую задачу
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": data.get("status", "pending")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# PUT /tasks/<id> — обновить задачу
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task.update(data)
    return jsonify(task)

# DELETE /tasks/<id> — удалить задачу
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"result": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)