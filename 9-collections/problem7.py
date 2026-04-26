# Using OrderedDict:

# Implement a LRU (Least Recently Used) Cache
# Fixed size cache (maxsize=3)
# When full, remove least recently used
# Operations:

# get(key) - returns value, updates to recent
# put(key, value) - adds item
# show() - displays cache

from collections import OrderedDict
class LRUCache:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.lru_cache = OrderedDict()

    def get(self, key):
        if key in self.lru_cache.keys():
            self.lru_cache.move_to_end(key)
            return self.lru_cache[key]
        return None

    def put(self, key, value):
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key)
        self.lru_cache[key] = value
        if len(self.lru_cache) > self.maxsize:
            self.lru_cache.popitem(last=False)
        self.lru_cache[key] = value

    def show(self):
        print("Output:")
        print("Cache (Most -> Least recent)")
        for key, value in reversed(self.lru_cache.items()):
            print(f"{key}: {value}")

cache = LRUCache(maxsize=3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
cache.get("a")      
cache.put("d", 4)   
cache.show()
