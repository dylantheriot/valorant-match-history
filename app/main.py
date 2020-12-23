from flask import Flask, render_template, request
from .valApi import ValorantAPI

app = Flask(__name__)

@app.route('/')
def home():

  return render_template('login.html')

#   return Response(json_res, mimetype="application/json")

@app.route('/login', methods=['POST'])
def login():
  username = request.form['username']

  return username