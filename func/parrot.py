# -*- coding: utf-8 -*-

import time
from flask import request, make_response
from xml.etree import ElementTree as ET

def parrot():
    xmlMsg = ET.fromstring(request.data)
    toUser = xmlMsg.find("ToUserName").text
    fromUser =  xmlMsg.find("FromUserName").text
    msgType = xmlMsg.find("MsgType").text

    if msgType == 'text':
        content = xmlMsg.find("Content").text
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
        response = make_response(reply % (fromUser, toUser, int(time.time()), content))
        response.content_type = 'application/xml'
        return response
    elif msgType == 'image':
        meidaId = xmlMsg.find("MediaId").text
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[image]]></MsgType><Image><MediaId><![CDATA[%s]]></MediaId></Image></PicUrl></xml>"
        response = make_response(reply % (fromUser, toUser, int(time.time()), meidaId))
        response.content_type = 'application/xml'
        return response
    else:
        return False
