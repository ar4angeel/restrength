from flask import Flask, request, jsonify
from tasks import heavy_computation
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=2)  # Для дополнительного кэширования

@app.route('/submit', methods=['POST'])
def submit_task():
    data = request.json
    n = data.get('n')
    if not isinstance(n, int) or n <= 0:
        return jsonify({"error": "Invalid input"}), 400

    task = heavy_computation.delay(n)
    return jsonify({
        "task_id": task.id,
        "status": "submitted"
    }), 202

@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    task_result = heavy_computation.AsyncResult(task_id)
    status = task_result.status
    result = task_result.result if task_result.ready() else None

    return jsonify({
        "task_id": task_id,
        "status": status,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)