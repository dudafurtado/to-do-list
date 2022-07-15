from flask import Flask, jsonify, request
from database import db
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def welcome():
  return jsonify("Welcome to the API of tasks made by Maria Eduarda Furtado! What do you think about see the list of tasks or just create one?")

@app.route('/tasks/list', methods=['GET'])
def list_tasks():
  return jsonify(db)

@app.route('/task/create', methods=['POST'])
def create_task():
  req_data = request.get_json()
  db.append(req_data)
  return jsonify("The task was created successfully. Congrats! What about create one more?")
