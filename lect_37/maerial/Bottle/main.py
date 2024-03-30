from bottle import Bottle, run, route, template, view

app = Bottle()


@app.route('/')
def index():
    return 'Привіт світ!'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Світ'):
    return template('temp', name=name)


@app.route('/view')
@app.route('/view/<name>')
@view('temp')
def hello(name='Світ'):
    return dict(name=name)


run(app, host='localhost', port=8070)
