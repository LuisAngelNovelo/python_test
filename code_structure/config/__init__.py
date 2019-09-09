# -*- coding: utf-8 -*-
"""
    config.flask
    ~~~~~~~~~~~~~~

    Setup Flask & Extensions

    :copyright: (c) 2019 by Software Clever, Palace Resorts CEDIS.
    :license: Private.
"""
from .flask import app
from .extensions.slave import slave
from .extensions.db import db
from .extensions.api import api
from .routes import *
