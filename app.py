from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)
started_at = datetime.now()

@app.route('/')
def hello():
    name = os.getenv("NAME", "Unknown")
    age = os.getenv("AGE", "Unknown")
    return f"Hello, I'm {name}. I'm {age}."