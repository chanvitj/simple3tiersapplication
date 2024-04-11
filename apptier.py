from flask import Flask
import requests
import json 

apptier = Flask(__name__)

@apptier.route('/')
def hello():
  url = "http://192.168.0.140:8001"
  headers = {'content_type': 'application/json'}
  method = 'GET'
  response = result = requests.request(method, url, headers=headers)
  if response.status_code == 200:
    data = response.json()
    data['additional information']='This is additional information from Web-Tier.'
    return data 
  else:
    return f"Error: {response.status_code}"

if __name__ == '__main__':
  apptier.run(host='0.0.0.0', port=8000)
