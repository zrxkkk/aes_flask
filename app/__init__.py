import flask
import datetime
from flask import request
import logging
import logging.config

from app import aes
from app import db


app = flask.Flask(__name__)


@app.route('/aes', methods=['POST', 'GET'])
def base():
    return flask.render_template('aes.html')

@app.route('/aes/encode', methods=['POST'])
def aes_encode():
    content = flask.request.form['encode']
    data = aes.encrypt(content)
    db.insert_aes('encode', content, data)
    return flask.render_template('aes.html', encode_result=data)


@app.route('/aes/decode', methods=['POST', 'GET'])
def aes_decode():
    if request.method == 'GET':
        return flask.render_template('decode.html')
    if request.method == 'POST':
        content = flask.request.form['decode']
        data = aes.decrypt(content)
        db.insert_aes('decode', content, data)
        return flask.render_template('decode.html', decode_result=data)


@app.route('/aes/history', methods=['GET'])
def aes_history():
    rows = db.fetchall_aes()
    data = []
    for dic in rows:
        data.append({
            'id': dic['id'],
            'time': datetime.datetime.fromtimestamp(dic['time']).strftime('%y-%m-%d %H:%M:%S'),
            'method': 'encode' if dic['method'] == 'encode' else 'decode',
            'content': dic['content'],
            'result': dic['result']
        })
    return flask.render_template('history.html', history_result=data)
