# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
import time
import pickle
from collections import namedtuple
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
import github3
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]



class Home(object):
    """."""

    #
    # Cache Construct for caching the home page data
    cache_construct = namedtuple('cache_construct', 'cached, catched_at, expiry_after')

    cache = cache_construct(
        catched_at=0,
        expiry_after=1,
        cached=None
    )

    def __init__(self, context):
        """."""
        self.context = context
        self.to_hours = 60 * 60

    def get_content(self):
        """."""
        _is_expired = self.__class__.cache.catched_at + \
            (self.__class__.cache.expiry_after * self.to_hours) <= time.time()

        if not self.__class__.cache.cached or _is_expired:
            self.__class__.cache = self.__class__.cache_construct(
                catched_at=time.time(),
                expiry_after=1,
                cached=github3.github.GitHub().user('sivacn').to_json()
            )

        return {
            'ip_addr': self.context.request.remote_addr,
            'github': self.__class__.cache.cached
        }


if __name__ == '__main__':
    """This Bolck is used for Unit Test.
    """
    pass
