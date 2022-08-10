import requests


def get_car_by_plate(plate):
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate}"
    resp = requests.get(endpoint)
    data = resp.json()
    car = data[0]
    return car


def random_cars_brand(brand):
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"
    resp = requests.get(endpoint)
    cars_list = resp.json()
    return cars_list