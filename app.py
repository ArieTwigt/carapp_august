# imported the Flask class
from flask import Flask, render_template
from custom_modules.api_functions import get_car_by_plate

# initiated application
app = Flask(__name__)

# defined a route
@app.route('/')
def hello():
    message = "Hello World"
    return render_template("index.html",
                           message=message)

# route for getting the car by plate
@app.route('/show_car')
def show_car():
    car = get_car_by_plate("TB725F")
    return render_template("show_car.html", car=car)


# execute/run the application
if __name__ == '__main__':
    app.run()