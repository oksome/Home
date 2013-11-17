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
            topic, messagedata = string.split()
            print(topic, messagedata)

if __name__ == '__main__':
    m = Minion(('8', '9'), 'tcp://localhost:5560')
    m.run()