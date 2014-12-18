#coding: utf-8

import json
from cnsiva import bottle
from cnsiva import config
from cnsiva.utils import SnippetFormatizer, JsonFormatizer

app = application = bottle.Bottle()

# Static pages

@app.route('/')
def index():
   """."""
   return views("frame_template.html")

@app.route('/get_page_content/<page_name>', method=['GET'])
def get_page_content(page_name):
    """."""
    if page_name in config.master_dict:
        file_name, file_type = config.master_dict.get(page_name)
    else:
        return sorry_page(page_name)

    _page_content = None

    if file_type == 'snippet':
        _page_content = get_snippet("""{0}.snippet""".format(file_name))
    elif file_type == 'json':
        _page_content = get_json("""{0}.json""".format(file_name))

    if not _page_content:
        return "No Content to be displayed !"

    return _page_content.replace(' ', '&nbsp;')

@app.route('/show_main_page', method=['GET'])
def show_main_page():
   """."""
   return "This is Main Page"

@app.route('/sorry_page/<page_name>', method=['GET'])
def sorry_page(page_name):
    """Serve sorry page"""
    return '<p>Requested page does not Exist:</p>'.format(page_name)

@app.get('/<filename:re:.*\.(tpl|html)>')
def views(filename):
    return bottle.static_file(filename, root='cnsiva/static/htmls')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return bottle.static_file(filename, root='cnsiva/static/js')

@app.get('/<filename:re:.*\.snippet>')
def get_snippet(filename):
    _snippet_object = bottle.static_file(filename, root='cnsiva/static/snippets')
    _page_content = SnippetFormatizer(_snippet_object).synthesis()

    return _page_content

@app.get('/<filename:re:.*\.json>')
def get_json(filename):
    _json_object = bottle.static_file(filename, root='cnsiva/static/json')
    _text_data = _json_object.body.readlines()
    _json_data = json.dumps(json.loads(''.join(_text_data)), indent=4, sort_keys=True).replace('\n', '<br>')
    _formatted_data = """<pre>{0}{1}{0}</pre>""".format("<br>"*20, _json_data)
    return _formatted_data

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
