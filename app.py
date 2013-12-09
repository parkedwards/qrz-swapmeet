from flask import Flask

class Config(object):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = '5000'

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return "works"

if __name__ == "__main__":
    app.run()
