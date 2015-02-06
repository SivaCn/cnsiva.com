#!/usr/bin/python


## ------------ Imports ----------- ##
import random
from config import quote_list
## ------------ Imports ----------- ##


class Quotes(object):
    """."""
    def __init__(self):
        """."""
        pass

    def __get_quote_number(self, available_domain):
        """."""
        if available_domain == 1:
            return 0

        return random.randint(0, int(available_domain) - 1)

    def __formatter(self, _quote, _author):
        """."""
        _template = """%(pre_processor)s
                       <h5><p align="center"><b>Quote on Open Source</b></p></h5>
                       %(pre_processor)s
                       <p align="center"><b>%(quote)s</b></p><br><br>
                       <p align="center">-- <b>%(author)s</b></p>"""

        _params = {'pre_processor': "<br>" * 2,
                   'quote': _quote,
                   'author': _author}

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
