# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]


class Home(object):
    """."""
    def __init__(self, context):
        """."""
        self.context = context

    def get_content(self):
        """."""
        _dict = {

        }
        return self.context.request.remote_addr


if __name__ == '__main__':
    """This Bolck is used for Unit Test.
    """
    pass
