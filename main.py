from flask import Flask, request
from faker import Faker
from utils import open_requirements, amount_of_astronauts, read_csv
import requests

app = Flask(__name__)

fake = Faker()


@app.route('/requirements/')
def requirements():
    return open_requirements()


@app.route('/generate-users/<number>')
def fake_data(number):
    generate_data = str()
    number = int(number)
    for i in range(number):
        generate_data += f'<p> {fake.first_name()} {fake.email()}'
    return generate_data


@app.route('/mean/')
def mean():
    return read_csv('hw.csv')


@app.route('/space/')
def space():
    return amount_of_astronauts()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
