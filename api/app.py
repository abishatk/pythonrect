from flask import Flask
from flask_cors import CORS,cross_origin
app = Flask(__name__)
cors=CORS(app, resources={r'*':{'origins':'https://localhost:3000'}})
CORS(app)

