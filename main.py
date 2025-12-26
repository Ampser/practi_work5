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

@app.route("/")
def index():
    name = "somchai <b>3 Sombut"
    time = datetime.now()
    return render_template('index.html', 
                           name=name, 
                           time=time,
                           news_items=news_items.values())

