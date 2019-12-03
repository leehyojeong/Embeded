# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:51:25 2019

@author: sejeong
"""

import paho.mqtt.publish as publish

publish.single("embeded/mqtt/project","PLAY",host="test.mosquitto.org")#mqtt서버에 연결