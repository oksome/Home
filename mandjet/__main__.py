
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

import cherrypy

from mandjet.root import Mandjet
from mandjet.hawk import Hawk

cherrypy.server.socket_host = '0.0.0.0'

hawk = Hawk()
root = Mandjet(hawk)

cherrypy.quickstart(root)
