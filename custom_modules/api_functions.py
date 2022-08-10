import requests


def get_car_by_plate(plate):
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate}"
    resp = requests.get(endpoint)
    