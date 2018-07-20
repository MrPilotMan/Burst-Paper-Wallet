from requests import post
from json import loads as json

def brs_api(request_type, arguments=""):
    url = "http://localhost:8125/burst?requestType={}{}".format(request_type, arguments)
    data = json((post(url)).text)
    return data