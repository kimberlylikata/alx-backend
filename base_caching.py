# base_caching.py

class BaseCaching:
    """BaseCaching defines a caching system"""
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache data"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
