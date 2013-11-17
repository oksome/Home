# Copyright (c) 2013 "OKso http://okso.me"
#
# This file is part of Home.
#
# Home is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
A Controller sends commands to Minions via the Intercom.
'''

import zmq
import random
import time
import json


def dump(string):
    return bytes(json.dumps(string), 'utf-8')


class Controller:

    def __init__(self, name, intercom='tcp://localhost:5559'):
        self.name = name
        self.intercom = intercom
        self.reset()

    def reset(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.connect(self.intercom)

    def send(self, topic, msg):
        if type(topic) != bytes:
            topic = bytes(str(topic), 'utf-8')
        messagedata = bytes(json.dumps(msg), 'utf-8')
        self.socket.send(topic + b' ' + messagedata)
        print(topic + b' ' + messagedata)


class SampleController(Controller):

    def on(self, action):
        topic = 'do:arduino.switch'

        msg = {'origin': self.name,
               'group': '00011',
               'plug': '10000',
               'action': action,
               }

        self.send(topic, msg)

if __name__ == '__main__':
    c = SampleController('bob')
    while True:
        c.on(input('action: '))
