README
------

NGINX

    This app is powerd by the NGNIX proxy server and load balancer

How to run this app ?

    $ uwsgi --enable-threads --http 0.0.0.0:8080 -w WSGI:app
