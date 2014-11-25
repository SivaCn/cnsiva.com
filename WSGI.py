#!/usr/bin/python

"""run this file using the following command

uwsgi --enable-threads --http 0.0.0.0:8080 -w WSGI:ap
"""

from run import app

if __name__ == '__main__':
    app.run()
