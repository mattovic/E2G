# -*- coding: utf-8 -*-

import hashlib
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/auth')
def authenticate():
    token = 'brandnewday'
    # fetch incoming arguments
    signature = request.args['signature']
    timestamp = request.args['timestamp']
    nonce = request.args['nonce']
    echostr = request.args['echostr']
    
    triplet = sorted([token, timestamp, nonce])
    sha1 = hashlib.sha1()
    tempstr = sha1.update(triplet[0] + triplet[1] + triplet[2])
    hashcode = sha1.hexdigest()

    if signature == hashcode:
        return echostr
    else:
        return False

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.7.101', port=10080)
