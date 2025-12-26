from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

news_items = {
    1: {'id': 1, 
        'title': 'COVID-19 update', 
        'body': 'This is a news on COVID-19'},
    2: {'id': 2, 
        'title': 'Facemasks found', 
        'body': 'Recent news on facemask production'},
    3: {'id': 3,
        'title':'Python 4', 
        'body':'Python 4 will be out soon.... this is FAKE'},
}

@app.route('/')
def index():
    name = 'Somchai'
    time = datetime.now()
    return render_template('index.html', 
                           name=name, 
                           time=time,
                           news_items=news_items.values())

@app.route('/news/<id>/')
def show_news_item(id):
    news_item = news_items[int(id)]
    return render_template('news_item.html',
                           id=news_item['id'],
                           title=news_item['title'],
                           body=news_item['body'])