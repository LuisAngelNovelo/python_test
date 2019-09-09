# -*- coding: utf-8 -*-
"""
    config.flask
    ~~~~~~~~~~~~~~

    Setup Flask

    :copyright: (c) 2019 by Software Clever, Palace Resorts CEDIS.
    :license: Private.
"""
from flask import Flask


ENVIRONMENT = "QA"
app = Flask(__name__)


class Config(object):
    """Required API Flask's settings"""

    #: Project config values
    SYSTEM_ID = 2
    TEMP_FOLDER = "/tmp"

    #: Sqlalchemy config values
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DBAPI = "mysql+pymysql"
    SQLALCHEMY_DATABASE = "clv_rates"
    SQLALCHEMY_PARAMS = {
        "local_infile": 1, "charset": "utf8"}

    #: App config values
    ENV = "production"
    DEBUG = False
    TESTING = False


class PROConfig(Config):
    #: App config values
    APP_ENV = "PRO"


class QAConfig(Config):
    #: App config values
    APP_ENV = "QA"


class DEVConfig(Config):
    #: App config values
    ENV = "development"
    DEBUG = True
    TESTING = True
    APP_ENV = "DEV"


#: Set Flask configs
if ENVIRONMENT == "PRO":
    app.config.from_object(PROConfig)
elif ENVIRONMENT == "QA":
    app.config.from_object(QAConfig)
else:
    app.config.from_object(DEVConfig)
