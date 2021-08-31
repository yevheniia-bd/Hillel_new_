import requests
import datetime
import json

city = 'Odessa'
days_amount = 5
Api_Id = 'f9ada9efec6a3934dad5f30068fdcbb8'
def receive_data():
    weather_data = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid='),
    params=("cnt": days_amount, "q": city, "Api_Id": API_key)
    return weather_data.json()
print(receive_data())

def work_with_data():
    weather_data = receive_data()
    print(weather_data['list'])
    resultat = []
    for day in weather_days["list"]:
        full_date = datetime.datetime.fromtimestamp(day['dt'])
        date = full_date.strftime("%d.%m.%Y")
        resultat.append(date)
        resultat.append(day['temp']['day'])
        resultat.append(day['feels_like']['day'])
        resultat.append(day['temp']['night'])
        weather_data.append(resultat)
return weather_data

def verified_data_for_file():
    insert_data = receive_data()
    use_date = datetime.datetime.fromtimestamp(insert_data['list'][0]['dt'])
    data = use_date.strftime("%d.%m.%Y")
    verified_data = f'{str(data)}-{insert_data["city"]["name"]}-{insert_data["cnt"]}
    print(verified_data)

def save_to_the_file():
    with open('weather_file', 'w') as file:
        for line in resultat:
            for i, val in enumerate(line):
                line(i) = val.ljust(15)
                file.write('    ',join(line) + '\n')


receive_data()
work_with_data()
verified_data_for_file()
save_to_the_file()

