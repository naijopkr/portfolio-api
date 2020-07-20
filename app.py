from flask import Flask, jsonify
from fetch_projects import fetch_projects
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/projects')
def projects():
    repos = fetch_projects()

    return jsonify(repos)
