from flask import Flask, jsonify, render_template, request, url_for

app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('index.html')
    #return 'Hello world' 

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/ready_load')
def ready_load():
    return render_template('ready_load.html')

if __name__ == '__main__':
	app.run(port=8090, host='0.0.0.0', debug=True)
