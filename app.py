# imported the Flask class
from flask import Flask
from custom_modules.api_functions import get_car_by_plate

# initiated application
app = Flask(__name__)

# defined a route
@app.route('/')
def hello():
    return "Hello Lisbon"

# route for getting the car by plate
@app.route('/show_car')
def show_car():
    car = get_car_by_plate("TB725F")
    return car


# execute/run the application
if __name__ == '__main__':
    app.run()