import requests
import json
URL = 'http://127.0.0.1:8000/student_api/'
headers = {'content-Type': 'application/json'}


def show_data(id=None):
    data = {
        'id': id,
    }
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data=json_data)
    print(r.json())


def create_data():
    data = {
        'id': 4,
        'name': 'Raj',
        'roll': 104,
        'city': 'Dhaka'

    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    print(r.json())


def update_data():
    data = {
        'id': 1,
        'name': 'Al Rony',
        'roll': 104,

    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    print(r.json())


def delete_data(id):
    data = {
        'id': id
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    print(r.json())


delete_data(1)
