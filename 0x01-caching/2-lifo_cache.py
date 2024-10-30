#!/usr/bin/env python3
"""
LIFO caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Representing an object that allows to store and
    retrieve items from a dict with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """
        Initializing the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adding an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lst_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lst_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Retrieving an item by key.
        """
        return self.cache_data.get(key, None)
