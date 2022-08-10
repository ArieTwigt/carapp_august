# imported the Flask class
from crypt import methods
from flask import Flask, render_template, request
from custom_modules.api_functions import get_car_by_plate, random_cars_brand

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

# route for returning a list of cars
@app.route('/show_random_cars', methods=['GET', 'POST'])
def show_random_cars():
    
    if request.method == 'POST':
        selected_brand = request.form.get('brand')
        cars = random_cars_brand(selected_brand)
        return render_template("random_cars_brand.html", cars=cars)
    
    return render_template("random_cars_brand.html")

# execute/run the application
if __name__ == '__main__':
    app.run()