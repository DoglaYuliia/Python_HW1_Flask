import csv
import requests
import pandas as pd



def open_requirements():
    with open('requirements.txt') as file:
        result = file.read()
    return result


def read_csv(file_csv):
    data = pd.read_csv(file_csv, delimiter=' *, *')
    height = data['"Height(Inches)"'].mean()
    weight = data['"Weight(Pounds)"'].mean()
    return (f'\t Средний рост: {str((height)  * 2.54)} cm</p>Средний вес: {str((weight) * 0.453592)} kg')


def amount_of_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    astros = r.json() ["number"]
    return f'Количество космонавтов: {astros}'