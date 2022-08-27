from flask import Flask
from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def home():
      return """Home page"""



def cat(filename):
    with open(filename) as file:
        data = file.read()
        return data



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"))