
import cherrypy

from mandjet.root import Mandjet
from mandjet.hawk import Hawk

cherrypy.server.socket_host = '0.0.0.0'

hawk = Hawk()
root = Mandjet(hawk)

cherrypy.quickstart(root)
