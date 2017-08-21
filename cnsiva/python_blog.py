# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
import json
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


class PythonBlog(object):

    """."""
    def __init__(self):
        """."""
        pass

    def get_page_content(self):
        """."""
        return json.dumps([
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
            {'title': 'blog post 1', 'content': 'content 1'},
        ])


if __name__ == '__main__':
    """This Bolck is used for Unit Test.
    """
    pass
