import time 
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"


@app.route('/api/jobs')
def get_jobs():
    jobs = [
        {"company": "Google", "status": "Applied"},
        {"company": "Amazon", "status": "Interview"}
    ]
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(port=5000)

