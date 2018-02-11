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

import os

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'fly-atlantic-api')

SENTINEL_MANAGEMENT_USERNAME = os.environ.get('SENTINEL_MANAGEMENT_USERNAME', '')
SENTINEL_MANAGEMENT_PASSWORD = os.environ.get('SENTINEL_MANAGEMENT_PASSWORD', '')
SENTINEL_MONGO_HOST = MONGO_HOST
SENTINEL_MONGO_PORT = MONGO_PORT
SENTINEL_MONGO_USERNAME = MONGO_USERNAME
SENTINEL_MONGO_PASSWORD = MONGO_PASSWORD
SENTINEL_MONGO_DBNAME = os.environ.get('SENTINEL_MONGO_DBNAME', 'oauth')
SENTINEL_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

X_DOMAINS = '*'

airports = {
    'item_title': 'airport',
    'additional_lookup': {
        'url': 'regex("[\w]{4}")',
        'field': 'icao'
    },
    'schema': {
        'icao': {
            'type': 'string',
            'minlength': 4,
            'maxlength': 4,
            'unique': True,
            'required': True
        },
        'location': {
            'type': 'point'
        },
        'elevation': {
            'type': 'integer'
        },
        'transitionaltitude': {
            'type': 'integer'
        }
    }
}
# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'airports': airports
}
