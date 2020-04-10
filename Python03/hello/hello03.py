#-*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_root():
    return '<a href="/test/admin">id</a>'


@app.route('/test/<id>')
def hello_id(id):
    return '<h1>hello,'+id+'</h1>'


if __name__ == '__main__':
    app.run()



