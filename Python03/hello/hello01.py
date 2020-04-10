#-*- coding:utf-8 -*-

'''
Flask 
cmd에 pip install flask
https://palletsprojects.com/p/flask/

'''

from flask import Flask
app= Flask(__name__)


@app.route('/')     #spring의 request mapping과 같음(url을 mapping 시켜준다)
def hello():
    return "Hello, Flask"


if __name__ == '__main__':
    app.run()


