from flask import Flask
import os

app = Flask(__name__)

@app.route('/')


def Default():
    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = fizz + buzz
    increment3 = 3
    increment5 = 5
    i = 0
    if i % increment3 == 0 and i % increment5 == 0:
        return fizzbuzz
    elif i % increment3 == 0:
        return fizz
    elif i % increment5 == 0:
        return buzz
    else:
        return i
    
Default()

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)


    app.run(port=port,host='0.0.0.0')
