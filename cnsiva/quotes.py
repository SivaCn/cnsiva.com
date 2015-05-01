#!/usr/bin/python


## ------------ Imports ----------- ##
import random
from config import quote_list
## ------------ Imports ----------- ##


class Quotes(object):
    """."""
    def __init__(self, context):
        """."""
        self.context = context

    def __get_quote_number(self, available_domain):
        """."""
        if available_domain == 1:
            return 0

        return random.randint(0, int(available_domain) - 1)

    def __formatter(self, _quote, _author):
        """."""

        _template = """
                    <div class="row">
                       <div class="eight columns titled outlined">
                           (venv)<br>
                           <b>cnsiva@OpenSource#</b> ~/scripts/./getRandomQuote.py<br>
                           %(pre_processor)s
                           <p align="center"><b>%(quote)s</b></p><br>
                           <p align="right">
                               -- <b>%(author)s</b>
                           </p>
                           (venv)<br>
                           <b>cnsiva@OpenSource#</b> <img src="/cursor_blink_1.gif" height="20" width="10">
                           <br>
                       </div>
                       <div class="three columns outlined">
                           <br>
                           %(user_info)s
                           <br>
                           <font size="-2" color="red"> <b>*** NOTE: No data is stored</b></font>
                       </div>
                    </div>"""

        _params = {'pre_processor': "<br>",
                   'quote': _quote,
                   'author': _author,
                   'user_info': None}

        _user_template = """<b>Your IP is </b>%(ip)s"""

        _user_info = {'ip': self.context.request.remote_addr or 'Unknown'}

        _params.update({'user_info': _user_template % _user_info})

        return _template % _params

    def get_quote(self):
        """."""
        total_available_quotes = len(quote_list)

        quote_to_get = self.__get_quote_number(total_available_quotes)

        _quote, _author = quote_list[quote_to_get]

        return self.__formatter(_quote, _author)


if __name__ == '__main__':
    """This Bolck is used for Unit Test.
    """
    pass
