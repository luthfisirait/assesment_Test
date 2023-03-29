import requests
import json
import coreapi
client = coreapi.Client()
schema = client.get("http://13.212.226.116:8000/docs/")
BASE_URL = 'http://13.212.226.116:8000'
def register_user(email, password,first_name,last_name,profile_image,address,city,province,country,telephone):
    data = {
        'username': email,
        'first_name':first_name,
        'last_name':last_name,
        'address':address,
        "city":city,
        "province":province,
        'country':country,
        'password': password,
        "telephone":telephone,
        "profile_image": profile_image
    }  
    action = ["register", "create"]
    schema = client.get("http://13.212.226.116:8000/docs/")
    result = client.action(schema, action, params=data)
    return result

def register_userv1(email, password,first_name,last_name,profile_image,address,city,province,country,telephone):
    url = f'{BASE_URL}/api/register/'
    data = {
        'username': email,
        'first_name':first_name,
        'last_name':last_name,
        'address':address,
        "city":city,
        "province":province,
        'country':country,
        'password': password,
        "telephone":telephone
        
    }
    files={"profile_image": profile_image}
    response = requests.post(url, data=data, files=files)
    return response.text


def get_access_token(username, password):
    action = ["api", "token > create"]
    params = {
        "username": username,
        "password": password,
    }
    result = client.action(schema, action, params=params)
    return result

def refresh_access_token(refresh_token):
    action = ["api", "token > refresh > create"]
    params = {
        "refresh": refresh_token,
    }
    result = client.action(schema, action, params=params)
    return result
def get_user_profile(access_token):
    action = ["profile", "list"]
    result = client.action(schema, action)
    return result
