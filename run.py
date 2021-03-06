#!/usr/bin/env python
"""
<one line to give the program's name and a brief idea of what it does.>
Copyright (C) 2017 Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of Fly Atlantic API.

Fly Atlantic API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Fly Atlantic API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Fly Atlantic API.  If not, see <http://www.gnu.org/licenses/>.
"""

from eve import Eve
import os
from oauth2 import BearerAuth
from flask_sentinel import ResourceOwnerPasswordCredentials, oauth

app = Eve(auth=BearerAuth)
ResourceOwnerPasswordCredentials(app)

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'
    debug = False
else:
    port = 5000
    host = '0.0.0.0'
    debug = True

if __name__ == '__main__':
	app.run(host=host, port=port, debug=debug)
