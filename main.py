#импортируем из библиотеки bottle нужные методы
from bottle import route, run, static_file
import os


@route('/hello')
def hello():
    return "Hello World!"


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, 'static/')
  
@route('/')
def root():
    return static_file('root.html', 'static/')

if os.environ.get('APP_LOCATION') == 'heroku':
	run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=8080, debug=True)
  
