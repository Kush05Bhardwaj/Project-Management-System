cache = {}

def get(key):
    return cache.get(key)

def set(key, value, ttl=None):
    cache[key] = value
    # Note: TTL handling is not implemented in this simple cache