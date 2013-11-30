from bottle import Bottle, request, redirect
import os
import sys

root = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sys.path.append(root)
sys.path.append(os.path.join(root, 'Intercom'))

from tumulus.tags import HTMLTags as t
from intercom.controller import Controller

import modules

app = application = Bottle()
controller = Controller('interface.Home')

@app.get('/')
def index():
    return t.html(
        t.body(
            t.h1('Home'),
            t.p('Home automation interface'),
            modules.plug('Bed',   '00001', '10000'),
            modules.plug('Mixer', '00001', '01000'),
            modules.plug('Ampli', '00001', '00100'),
            modules.plug('Desk',  '00001', '00010'),
        ),
    ).build()

@app.post('/api/switch')
def switch():
    plug = request.forms.get('plug')
    action = request.forms.get('action')
    controller.send('do:arduino.switch', {'action': action, 'group': '00001', 'plug': plug})
    redirect('/')
    #return t.html(
    #    t.body(
    #        t.p('Done'),
    #    ),
    #).build()


if __name__ == '__main__':
    app.run(host='0.0.0.0', reloader=True, debug=True)

