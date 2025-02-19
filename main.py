from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is Shamail Aamir Khan class activity 1"

if __name__ == '__main__':
    app.run()