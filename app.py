# imported the Flask class
from flask import Flask

# initiated application
app = Flask(__name__)

# defined a route
@app.route('/')
def hello():
    return "Hello world"


# execute/run the application
if __name__ == '__main__':
    app.run()