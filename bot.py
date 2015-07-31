# -*- coding: utf-8 -*-

import threading

import requests

from api import *


class Bot(object):
    def __init__(self, token, handler):
        self.token = token
        self.handler = handler
        self.is_working = False
        self.r = None

        self.worker = threading.Thread(target=self.loop)
        self.worker.daemon = False

    def loop(self):
        self.is_working = True
        offset = 1

        while self.is_working:
            self.r = requests.get(API % (self.token, GET_UPDATES + "?timeout=120&offset=" + str(offset)))
            json = self.r.json()

            if offset is 1 and json is not None and len(json["result"]) > 0:
                offset = int(json["result"][0]["update_id"])
            else:
                offset += 1

            self.handler(json)

    def start(self):
        self.worker.start()

    def stop(self):
        self.is_working = False

        if self.r is not None:
            self.r.close()
