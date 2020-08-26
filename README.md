# Coordinates-on-the-map
API service allows to query the nearest neighbors to given coordinates (x, y) within a radius of M kilometers.

## Для начала работы с api необходимо:

1. Установить все зависимости 
`$ pip install -r requirements.txt`
2. Запустить сервер базы данных - PostgreSQL, убедиться что БД пуста (при первом включении)
3. В файле config.json записать параметры забуска БД и сервера:

		    {"server":{"host": "Хост сервера", 
                       "port": "Порт Сервера"}, 
             "Data_Base":{"dbname": "Имя БД", 
                   	 	  "user": "Пользователь", 
                     	  "password": "Пароль", 
                    	  "host":"Хост сервера"}
4. Выполнить в терминале команды: 

		$ make build
		ok
		$ make test
		ok
		$ make run
	После этого будет запущен сервер и api готов к работе.

## Начало работы с api
Примеры работы:

Все примеры написанны на python3 c использованием модуля requests


### Вывод ближайших соседей к данным координатам долготы и широты в радиусе N километров:
longitude - долгота, longitude - широта(в радианах),
radius - в километрах

    def get_users(latitude, longitude, radius):
        url = r'http://127.0.0.1:8888//api/v0.1/get_users'
        data = {'latitude': latitude, 'longitude': longitude, 'radius': radius}
        status = requests.post(url, json=data)
        return status.json()


### Добавление новой точки:

    def add_user(latitude, longitude):
        url = r'http://127.0.0.1:8888//api/v0.1/add_user'
        data = {'latitude': latitude, 'longitude': longitude}
        status = requests.post(url, json=data)
        return status.json()

### Обновление информации о точке:
Для обновления, необходимо знать уникальный id точки, и ввести новые координаты

    def update_user(user_id, latitude, longitude):
        url = r'http://127.0.0.1:8888//api/v0.1/update_user'
        data = {'user_id': user_id,
                'latitude': latitude, 
                'longitude': longitude}
        status = requests.post(url, json=data)
        return status.json()

### Удаление точки:
Для удаления, необходимо знать уникальный id точки

    def delete_user(user_id):
        url = r'http://127.0.0.1:8888//api/v0.1/delete_user'
        data = {'user_id': user_id}
        status = requests.post(url, json=data)
        return status.json()

