from flask import Flask
from flask import render_template

# root -> '/'
# increment -> '/increment'
# decrement -> '/decrement'

app = Flask(__name__)
database = {}

if 'number' not in database:
    database['number'] = 0

@app.route('/')
def home():
    return render_template('index.html', number=database['number'])

@app.route('/increment')
def increment():
    # increments a number
    database['number'] += 1
    return render_template('index.html', number=database['number'])

@app.route('/decrement')
def decrement():
    # decrements a number
    database['number'] -= 1
    return render_template('index.html', number=database['number'])

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8083)