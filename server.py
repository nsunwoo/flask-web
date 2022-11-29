from flask import Flask
import random

app = Flask(__name__)


topics = [
    {'id': 1, 'title': 'HTML', 'body': 'HTML is ...'},
    {'id': 2, 'title': 'CSS', 'body': 'CSS is ...'},
    {'id': 3, 'title': 'JavaScript', 'body': 'JavaScript is ...'}
]
# 데이터베이스로 바꿀 예정


def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''


def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags


@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')


@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')


@app.route('/create/')
def create():
    return 'Create'


app.run(debug=True)