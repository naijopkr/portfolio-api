from flask import Flask, jsonify
from fetch_projects import fetch_projects

app = Flask(__name__)

@app.route('/projects')
def projects():
    repos = fetch_projects()

    return jsonify(repos)
