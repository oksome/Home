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
A Minion is an network endnode, connected to some input/output gadgets.
'''

import zmq
import json
import serial


class Minion:

    def __init__(self, topics, intercom='tcp://localhost:5560'):
        self.topics = topics
        self.intercom = intercom
        self.reset()

    def reset(self):
        # Socket to talk to server
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        print("Collecting updates from server...")
        self.socket.connect(self.intercom)
        for topic in self.topics:
            self.socket.setsockopt(zmq.SUBSCRIBE, bytes(topic, 'utf-8'))

    def run(self):
        while True:
            string = self.socket.recv()
            topic, messagedata = string.split(b' ', 1)
            topic = str(topic, 'utf-8')
            msg = json.loads(str(messagedata, 'utf-8'))
            self.receive(topic, msg)

    def receive(self, topic, msg):
        print(topic, msg)


class ArduinoMinion(Minion):
    '''
    This Minion talks to an Arduino running 'hawk.ino'.
    '''

    def __init__(self, topics, intercom):
        super(ArduinoMinion, self).__init__(topics, intercom)
        self.serial = serial.Serial('/dev/ttyUSB0')

    def receive(self, topic, msg):
        if 'action' in msg:
            switch_group = bytes('n' + msg['group'], 'utf-8')
            switch_plug = bytes('p' + msg['plug'], 'utf-8')
            instruction = {'on': b'w1', 'off': b'w0'}[msg['action']]

            print(switch_group + switch_plug + instruction)
            self.serial.write(switch_group + switch_plug + instruction)
        else:
            print('Unknown: ', msg)

if __name__ == '__main__':
    m = ArduinoMinion(('do:arduino.switch', 'do:arduino.read'), 'tcp://localhost:5560')
    m.run()