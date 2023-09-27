from flask import Flask, request, jsonify
import json
import requests
from routing import routes

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(routes)
    
# @app.route('/')
# def hello_world():
#     return 'Hello SBRP!'

if __name__ == '__main__':
    app.run(debug=True)

# To obtain parameters from config
# app.config["DB_HOST"] where key = key in config