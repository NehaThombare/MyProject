from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "Online",
        "message": "Microservice is running smoothly!",
        "timestamp": datetime.datetime.now().isoformat(),
        "environment": os.getenv("APP_ENV", "Development")
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "health": "healthy"
    }), 200

if __name__ == '__main__':
    # Running on 0.0.0.0 allows the app to accept connections from outside its container
    app.run(host='0.0.0.0', port=5000)