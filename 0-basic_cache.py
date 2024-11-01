# 0-basic_cache.py

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """BasicCache class - A caching system without a limit"""

    def put(self, key, item):
        """Assigns the item value to the key in cache_data dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to the key in cache_data"""
        return self.cache_data.get(key, None)
