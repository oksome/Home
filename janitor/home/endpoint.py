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

import zmq
import json

from django.conf import settings

zmq_context = zmq.Context()


def send_home(topic, msg):
    '''
        Send a message to the ZMQ backend.
        `topic` will be used for the backend PUB/SUB.
    '''
    if type(topic) != bytes:
        topic = bytes(str(topic), 'utf-8')
    messagedata = bytes(json.dumps(msg), 'utf-8')

    socket = zmq_context.socket(zmq.REQ)
    socket.connect(settings.INTERCOM_ENDPOINT)
    socket.send(topic + b' ' + messagedata)
    print(topic + b' ' + messagedata)
    reply = socket.recv()
    print('reply', reply)
