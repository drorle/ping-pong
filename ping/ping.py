from flask import Flask
app = Flask(__name__)
@app.route('/pong')
def pong():
    return 'PING', 200
if __name__ == '__main__':
    app.run('0.0.0.1', debug=True)