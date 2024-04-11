from flask import Flask

webtier = Flask(__name__)


@webtier.route('/')
def hello():
  r = {"id": 1, "title": "This is JSON data from App-Tier."}
  return r 

if __name__ == '__main__':
    webtier.run(host='0.0.0.0', port=8001)
