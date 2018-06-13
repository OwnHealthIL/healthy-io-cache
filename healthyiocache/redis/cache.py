from redis import Redis
import json

class Cache:
    def __init__(self, cache_configs):
        self.cache_ttl = cache_configs['ttl']
        self.cache = Redis(host=cache_configs['host'], port=cache_configs['port'], password=cache_configs['password'])

    def get(self, key):
        value = self.cache.get(key)
        try:
            json_value = json.loads(value)
        except (ValueError,TypeError):
            return value
        return json_value

    def put(self, key, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        self.cache.set(key, value, self.cache_ttl)

    def delete(self, key):
        self.cache.delete(key)