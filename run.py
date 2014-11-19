#coding: utf-8

import bottle

# Static pages

@bottle.route('/')
def index():
   """."""
   return views("frame_template.html")

@bottle.route('/get_page_content/<page_name>', method=['GET', 'POST'])
def get_page_content(page_name):
   """."""
   import pdb; pdb.set_trace()
   print page_name

@bottle.route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p>'

@bottle.get('/<filename:re:.*\.(tpl|html)>')
def views(filename):
    return bottle.static_file(filename, root='static/htmls')

@bottle.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return bottle.static_file(filename, root='static/js')

@bottle.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='static/css')

@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='static/images')

##  Web application main  # #
def main():

    # Start the Bottle webapp
    bottle.debug(True)
    bottle.run(host='0.0.0.0', port=80, reloader=True)

if __name__ == "__main__":
    print ">>>>"
    main()

