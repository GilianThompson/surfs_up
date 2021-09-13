from flask import Flask

#create a new flask app instance
app = Flask(__name__)

#first route, "root" 
@app.route('/')
def hello_world():
    return "Hello World"



