# -*- coding: utf-8 -*-
"""
    config.extensions.db
    ~~~~~~~~~~~~~~

    Setup DB

    :copyright: (c) 2019 by Software Clever, Palace Resorts CEDIS.
    :license: Private.
"""


from config import app
from config import slave
from flask_sqlalchemy import SQLAlchemy


__all__ = ["db"]


def setup_db_config():
    """ Retrieves DB connection """

    db_uri = slave.get_db_uri()
    app.config.update({"SQLALCHEMY_DATABASE_URI": db_uri})


setup_db_config()
db = SQLAlchemy(app)
