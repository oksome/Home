
import cherrypy

from mandjet.hawk import Plug


class Mandjet():

    def __init__(self, hawk):
        self.hawk = hawk
        self.places = {
            'desk':   Plug(hawk, '00001', '00010'),
            'bed':    Plug(hawk, '00001', '10000'),
            'mixer':  Plug(hawk, '00001', '01000'),
            'ampli':  Plug(hawk, '00001', '00100'),
        }
    
    @cherrypy.expose
    def index(self):
        result = '<ul>'
        for place in self.places:
            result += '''
                <li>
                    {}
                    <a href="/switch/{}/on">ON</a>
                    <a href="/switch/{}/off">OFF</a>
                </li>
            '''.format(place, place, place)
        return result

    @cherrypy.expose
    def switch(self, name, mode):
        #assert cherrypy.request.method == 'POST'
        if mode == 'on':
            self.places[name].on()
        elif mode == 'off':
            self.places[name].off()
        else:
            raise cherrypy.HTTPError(403)
        raise cherrypy.HTTPRedirect('/') 
