
# Copyright (c) 2013 "OKso http://okso.me"
# 
# This file is part of Ra.
# 
# Ra is free software: you can redistribute it and/or modify
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


import serial


class Hawk:
    
    def __init__(self):
        self.serial = serial.Serial('/dev/ttyUSB0')

    def network(self, id):
        msg = 'n{}'.format(id)
        self.serial.write(bytes(msg, 'utf-8'))

    def plug(self, id):
        msg = 'p{}'.format(id)
        self.serial.write(bytes(msg, 'utf-8'))

    def on(self):
        self.serial.write(b('w1'))

    def off(self):
        self.serial.write(b('w0'))

    def write(self, msg):
        self.serial.write(msg)


class Plug:
    
    def __init__(self, hawk, network_id, plug_id, status=None):
        self.hawk = hawk
        self.network_id = bytes('n' + network_id, 'utf-8')
        self.plug_id = bytes('p' + plug_id, 'utf-8')
        self.status = status

    def on(self):
        print(self.network_id + self.plug_id + b'w1')
        self.hawk.write(self.network_id + self.plug_id + b'w1')
        self.status = True

    def off(self):
        self.hawk.write(self.network_id + self.plug_id + b'w0')
        self.status = False
    
    def enforce(self):
        assert self.status is not None
        if self.status == True:
            self.on()
        else:
            self.off()
