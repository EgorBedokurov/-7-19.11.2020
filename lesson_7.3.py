import requests
import datetime

URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'


def day_val():              #выбор кол-ва дней
    day = int(input('set the number of days - '))
    return day


def daily_weath(days=1):
    data = {'q': 'Odessa', 'units': 'metric', 'cnt': days,
            'appid': 'f9ada9efec6a3934dad5f30068fdcbb8'}
    r = requests.get(URL, data)
    return r.json()


result = daily_weath(days=day_val())
with open('d_w.txt', 'w') as f:
    f.writelines(['    Date', '        Day', '     Night', '\n'])
    for day in result['list']:
        f.writelines([datetime.date.fromtimestamp(day['dt']).strftime('%d-%m-%Y') + (5 * ' '),
                      '{:.2f}'.format(day['temp']['day']) + (' ' * 6),
                      '{:.2f}'.format(day['temp']['day']) + (' ' * 6), '\n'])
