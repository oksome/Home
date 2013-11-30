from bottle import Bottle, request
import os
import sys

root = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
sys.path.append(root)
sys.path.append(os.path.join(root, 'Intercom'))

from tumulus.tags import HTMLTags as t
from intercom.controller import Controller

app = application = Bottle()
controller = Controller('interface.Home')

@app.get('/')
def index():
    return t.html(
        t.body(
            t.h1('Hello'),
            t.p('Hello world'),
            t.form(
                'Bed',
                t.input(name='plug', value='10000', type='hidden'),
                t.input(name='action', value='on', type='submit'),
                t.input(name='action', value='off', type='submit'),
                method='POST',
                action='/api/switch',
            )
        ),
    ).build()

@app.post('/api/switch')
def switch():
    plug = request.forms.get('plug')
    action = request.forms.get('action')
    controller.send('do:arduino.switch', {'action': action, 'group': '00001', 'plug': plug})
    return t.html(
        t.body(
            t.p('Done'),
        ),
    ).build()


if __name__ == '__main__':
    app.run(host='0.0.0.0', reloader=True, debug=True)

