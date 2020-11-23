"""
... GOOGLE CLOUD VERSION
    execute this module to start webserver.
    Access http://localhost:5000/<route>.
    e.g.: http://localhost:5000/deck
"""
import os, json
from flask import Flask, request
from ICEBreaker import ICEBreaker

app = Flask(__name__)
# app.config["thisGame"] = Game()
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
