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

import os
import time

import cherrypy

from mandjet.hawk import Plug


class Mandjet():

    def __init__(self, hawk):
        self.hawk = hawk
        self.places = {
            'desk':    Plug(hawk, '00001', '00010'),
            'bed':     Plug(hawk, '00001', '10000'),
            'mixer':   Plug(hawk, '00001', '01000'),
            'ampli':   Plug(hawk, '00001', '00100'),
            'kitchen': Plug(hawk, '00011', '10000'),
            'sink':    Plug(hawk, '00011', '01000'),
            'boiler':  Plug(hawk, '00011', '00010'),
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
        result += '<a href="/wakeup">Wake Up</a> <br/><a href="/sleep">Sleep</a>'
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

    @cherrypy.expose
    def wakeup(self):
        self.places['mixer'].on()
        self.places['ampli'].on()
        os.system('mpc play')
        time.sleep(10)
        self.places['desk'].on()
        time.sleep(10)
        self.places['bed'].on()
        return 'Good morning'

    @cherrypy.expose
    def sleep(self):
        os.system('mpc stop')
        self.places['bed'].off()
        self.places['desk'].off()
        self.places['ampli'].off()
        self.places['mixer'].off()
        return 'Good night'
