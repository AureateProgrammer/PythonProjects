import time 
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(port=5000)

def main():
    print('Give me a second printing time.....',)
    time.sleep(3)
    print(time.asctime())
main()

