#coding: utf-8

import json
from cnsiva import bottle
from cnsiva import config

app = application = bottle.Bottle()

# Static pages

@app.route('/')
def index():
   """."""
   return views("frame_template.html")

@app.route('/get_page_content/<page_name>', method=['GET'])
def get_page_content(page_name):
   """."""
   if not 'page_name' in config.json_list:
      return "<p>OOPS! You have discovered a BUG, please let me know about this!</p>"
   return get_json(config.json_list.get(page_name))

@app.route('/sorry_page', method=['GET'])
def sorry_page():
    """Serve sorry page"""
    _page_requested = bottle.request.params.get('get_page', '')
    return '<p>Requested: {0}</p>'.format(_page_requested)

@app.get('/<filename:re:.*\.(tpl|html)>')
def views(filename):
    return bottle.static_file(filename, root='cnsiva/static/htmls')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return bottle.static_file(filename, root='cnsiva/static/js')

@app.get('/<filename:re:.*\.json>')
def get_json(filename):
    _json_object = bottle.static_file(filename, root='cnsiva/static/json')
    _text_data = _json_object.body.readlines()
    return "<pre>" + json.dumps(json.loads(''.join(_text_data)), indent=4, sort_keys=True).replace('\n', '<br>') + "</pre>"

@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='cnsiva/static/css')

@app.get('/<filename:re:.*\.(jpg|jpeg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='cnsiva/static/images')

##  Web application main  # #
def main():

    # Start the Bottle webapp
    # bottle.debug(True)
    app.run(host='0.0.0.0', port=8080, reloader=True)

if __name__ == "__main__":
    main()
