# Coordinates-on-the-map
REST API сервис для поиска ближайших соседей на 2d плоскости. Основная функция - сервис позволяет запросить K ближайших соседей к данным координатам (x, y) в радиусе M километров.


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

## Работать с API можно 
1) через post запросы 
2) с помощью интерфейса

## 1)
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

## 2)

Для просмотра веб-страницы необходимо:
- в файле: `Application\scripts\server\static\js\send_post.js` заменить host и порт на свои. 
- перейти по ссылке http://host:port/api/v2/web_get_users/, где host и port заменить на свои.

![main](https://github.com/Ovsienko023/Coordinates-on-the-map/blob/master/Application/client/Screen/main_web_get_users.png)

Затем ввести корректные данные: широту`(рад)`, долготу`(рад)` и радиус `(км)` и нажать кнопку `SHOW`

![map](https://github.com/Ovsienko023/Coordinates-on-the-map/blob/master/Application/client/Screen/map_web_get_users.png)