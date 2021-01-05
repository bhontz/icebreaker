"""
    Assuming you have a localhost setup on your machine (visit http://localhost from within your browser to confirm)
    Start this module to create your webserver.

    Using this project with Thunkable will require hosting on a cloud service such as Heroku or Google Cloud, or
    using NGROK to tunnel your localhost out to the internet. (see: https://www.ngrok.com).
"""
import os, json
from flask import Flask, request
from ICEBreaker import ICEBreaker

app = Flask(__name__)
game = ICEBreaker()

@app.route('/count', methods=['GET'])
def getCount():
    return json.dumps(game.getCount())

@app.route('/question', methods=['GET'])
def getQuestion():
    item = request.args.get('item', default=-1, type=int)
    return game.getQuestion(item)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)

