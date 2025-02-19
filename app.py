from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is Shamail Aamir Khan 21I-1772  "

if __name__ == '__main__':
    app.run()
