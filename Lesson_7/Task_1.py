import requests
import datetime

city = 'Odessa'
days_amount = 5
Api_Id = 'f9ada9efec6a3934dad5f30068fdcbb8'
def receive_data():
    weather_data = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid='),
    params=("cnt": days_amount, "q": city, "Api_Id": API_key))
    return weather_data.json()

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

print(resultat)

with open('weather_file', 'w') as file:
    for line in resultat:
        for i, val in enumerate(line):
            line(i) = val.ljust(15)
        file.write('    ',join(line) + '\n')
