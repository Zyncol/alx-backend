#!/usr/bin/env python3
"""
Basic caching module for task 1
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Representing an object that allows to store and
    retrieve items from a dictionary.
    """
    def put(self, key, item):
        """
        Adding an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieving an item by key
        """
        return self.cache_data.get(key, None)
