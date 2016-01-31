# -*- coding: utf-8 -*-

import time
import sqlite3
from flask import make_response, request
from xml.etree import ElementTree as ET

def response():
    connection = sqlite3.connect('/projects/e2g/merchandise.db')
    cur = connection.cursor()
    xmlMsg = ET.fromstring(request.data)
    toUser = xmlMsg.find("ToUserName").text
    fromUser =  xmlMsg.find("FromUserName").text
    msgType = xmlMsg.find("MsgType").text
    if msgType == 'text':
        result = []
        content = xmlMsg.find("Content").text
        result_object = cur.execute("select category_name from makeups where merchandise_id in (select merchandise_id from merchandises where merchandise_name = '%s');" % content)
        for category_name in result_object:
                category = category_name[0]
                result.append(category)
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
        response = make_response(reply % (fromUser, toUser, int(time.time()), result))
        response.content_type = 'application/xml'
        return response
    else:
        return False
