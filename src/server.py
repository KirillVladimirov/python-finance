from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello, World!'


@app.route('/hello')
def hello_world(user=None):
    user = user or 'Shalabh'
    return '''
    <html>
        <head>
            <title>Templating in Flask</title>
        </head>
        <body>
            <h1>Hello %s!</h1>
            <p>Welcome to the world of Flask!</p>
        </body>
    </html>''' % user


@app.route('/hello_jinja')
def hello_jinja(user=None):
    user = user or 'Shalabh'
    navigation = [{'href':'home', 'caption': 'home'},
                  {'href':'root', 'caption': 'root'},
                  {'href':'about', 'caption': 'about'}]
    name = "hello new <i>world</i>"
    return render_template('t1_jinja.html',
                           user=user,
                           navigation=navigation,
                           a_variable=4,
                           name=name,
                           something=True)


@app.route('/child')
def child():
    return render_template('t2_jinja_child.html')


@app.route('/child2')
def child2():
    return render_template('t3_jinja_child2.html')


@app.route('/use_macros')
def use_macros():
    return render_template('t4_jinja_use_macros.html')
