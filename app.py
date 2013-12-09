import re
from flask import Flask, render_template, jsonify, abort
from requests import get
from bs4 import BeautifulSoup

class Config(object):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = '5000'

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    req = get('http://www.qrz.com')
    if req.ok:
        soup = BeautifulSoup(req.text)
        swlist = soup.find('div', {'class': 'swlist'})
        links = swlist.findAll('a', {'class': 'sl'})
        data = []
        for link in links:
            if not re.search('wanted', link['title'], re.I) \
                and not re.search('wtb', link['title'], re.I) \
                and not re.search('want to buy', link['title'], re.I):
                data.append((link['title'], link['href']))
        return render_template('index.html', data=data)
    else:
        abort(500)

if __name__ == "__main__":
    app.run('0.0.0.0')
