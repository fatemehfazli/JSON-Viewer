import requests
from pprint import pprint

def jsonViwer(url):    
    response = requests.get(url)
    
    if (
        response.status_code != 204 and
        response.headers["content-type"].strip().startswith("application/json")
    ):
        # try:
        pprint(response.json())
    else: 
        print("error")
        print(response.text)
url = input("Enter your url: ")
jsonViwer(url)