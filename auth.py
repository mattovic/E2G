# -*- coding: utf-8 -*-

import hashlib
import time
from flask import Flask, request, make_response
from xml.etree import ElementTree as ET

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'GET':
        token = 'brandnewday'
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
    	xmlMsg = ET.fromstring(request.data)
    	toUser = xmlMsg.find("ToUserName").text
    	fromUser =  xmlMsg.find("FromUserName").text
    	content = xmlMsg.find("Content").text
    	reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
    	response = make_response(reply % (fromUser, toUser, int(time.time()), content))
        response.content_type = 'application/xml'
    	return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.7.101', port=10080)
