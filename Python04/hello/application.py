#-*- coding:utf-8 -*-

#기본적으로 사용하는 
# spring에서의 controller 역할
# template에는 html 파일들이 들어간다
# static에는 css, js가 들어간다

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def root():
    return '''
        <a href="/hello">hello</a><br>
        <input type="button" value="hello" onclick="location.href='/hello/name'">
    '''

    
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/test', methods=['post'])
def test():
    return render_template('test.html',test=request.form['command'])


    
if __name__ == '__main__':
    app.run('localhost',port='8585')









