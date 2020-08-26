import requests

latitude = 48.704578 
longitude = 44.507112 
radius = 5

def get_users(latitude, longitude, radius):
    url = r'http://127.0.0.1:8888//api/v0.1/get_users'
    data = {'latitude': latitude, 'longitude': longitude, 'radius': radius}
    status = requests.post(url, json=data)
    return status.json()

print(get_users(latitude, longitude, radius))
