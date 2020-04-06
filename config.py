import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2MK1tt4XglJ8f8bSQ8RVZc2j'
