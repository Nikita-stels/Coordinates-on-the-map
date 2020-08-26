import requests

latitude = 48.704578
longitude = 44.507112 
radius = 5

def get_users(latitude, longitude, radius):
    url = r'http://127.0.0.1:8888//api/v0.1/get_users'
    data = {'latitude': latitude, 'longitude': longitude, 'radius': radius}
    status = requests.post(url, json=data)
    return status.json()

# print(get_users(latitude, longitude, radius))


def add_user(latitude, longitude):
    url = r'http://127.0.0.1:8888//api/v0.1/add_user'
    data = {'latitude': latitude, 'longitude': longitude}
    status = requests.post(url, json=data)
    return status.json()

latitude = 47.704578
longitude = 44.557112 
# print(add_user(latitude, longitude))

def delete_user(user_id):
    url = r'http://127.0.0.1:8888//api/v0.1/delete_user'
    data = {'user_id': user_id}
    status = requests.post(url, json=data)
    return status.json()

user_id = 8
# print(delete_user(user_id))



def update_user(user_id, latitude, longitude):
    url = r'http://127.0.0.1:8888//api/v0.1/update_user'
    data = {'user_id': user_id,
            'latitude': latitude, 
            'longitude': longitude}
    status = requests.post(url, json=data)
    return status.json()

latitude = 51.704578
longitude = 50.557112 
print(update_user(user_id, latitude, longitude))