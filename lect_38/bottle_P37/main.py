from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
def index():
    return 'Hello world'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello {name}'

@app.route('/reg/<name:re:[a-z]+>')
def hello_2(name):
    return name

@app.route('/html')
def render_html():
    return template('temp')

run(app, host='localhost', port=8070)