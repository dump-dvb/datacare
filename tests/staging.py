import requests
import json 
import logging
import http.client as http_client

import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

register_form = {
    "name": "foobar",
    "email": get_random_string(8) + "@example.com",
    "password": "testtesttest"
}

login_form = {
    "email": "test@test.com",
    "password": "test"
}

update_form = {
    "id": "fill_me",
    "name": "SuccessFullTest",
    "role": 9,
}

# this enables higly verbose logging for debug purposes
#http_client.HTTPConnection.debuglevel = 1
#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

with requests.Session() as s:
    create_user_response = s.post('https://datacare.staging.dvb.solutions/user/register', json = register_form)
    print(create_user_response)
    print(create_user_response.headers)
    print(create_user_response.content)

    list_user_response = s.get('https://datacare.staging.dvb.solutions/user/info')
    print(list_user_response)
    print(list_user_response.content)

    logout_user_response = s.post('https://datacare.staging.dvb.solutions/user/logout')
    print(logout_user_response)
    print(logout_user_response.content)

    login_user_response = s.post('https://datacare.staging.dvb.solutions/user/login', json = login_form)
    print(login_user_response)
    print(login_user_response.content)

    list_user_response = s.get('https://datacare.staging.dvb.solutions/user/list')
    print(list_user_response)
    print(list_user_response.content)
    
    update_form["id"] = json.loads(create_user_response.content)["id"]
    print(update_form)
    update_user_response = s.put('https://datacare.staging.dvb.solutions/user/update', json = update_form)
    print(update_user_response)
    print(update_user_response.content)

    delete_user_response = s.delete('https://datacare.staging.dvb.solutions/user/delete', json = {"id": update_form["id"]})
    print(delete_user_response)
    print(delete_user_response.content)




