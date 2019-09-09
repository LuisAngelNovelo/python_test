# -*- coding: utf-8 -*-
"""
    config.extensions.db
    ~~~~~~~~~~~~~~

    Setup API

    :copyright: (c) 2019 by Software Clever, Palace Resorts CEDIS.
    :license: Private.
"""


from config import app
from config import slave
from flask_restful import Api


__all__ = ["api"]


api = Api(app, catch_all_404s=True, errors=slave.werkzeug_errors())
