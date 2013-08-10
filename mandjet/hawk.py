
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
    
    def __init__(self, hawk, network_id, plug_id):
        self.hawk = hawk
        self.network_id = bytes('n' + network_id, 'utf-8')
        self.plug_id = bytes('p' + plug_id, 'utf-8')

    def on(self):
        print(self.network_id + self.plug_id + b'w1')
        self.hawk.write(self.network_id + self.plug_id + b'w1')

    def off(self):
        self.hawk.write(self.network_id + self.plug_id + b'w0')
