import unittest
from unittest import mock
from healthyiocache.redis.cache import Cache
import json


class TestCache(unittest.TestCase):
    @mock.patch('healthyiocache.redis.cache.Redis')
    def test_get(self, cache_client_mock):
        redis_instance_mock = mock.Mock()
        cache_client_mock.return_value = redis_instance_mock
        cache = Cache({'host': 'host', 'port': 'port', 'ttl': 'ttl'})
        cache_client_mock.assert_called_once_with(host='host', port='port')

        value = {'value': 'value'}
        redis_instance_mock.get.return_value = json.dumps(value)

        result = cache.get('key')

        assert result == {'value': 'value'}
        redis_instance_mock.get.assert_called_once_with('key')

    @mock.patch('healthyiocache.redis.cache.Redis')
    def test_put(self, cache_client_mock):
        redis_instance_mock = mock.Mock()
        cache_client_mock.return_value = redis_instance_mock
        cache = Cache({'host': 'host', 'port': 'port', 'ttl': 'ttl'})
        cache_client_mock.assert_called_once_with(host='host', port='port')

        cache.put('key', {'value': 'value'})

        value = {'value': 'value'}
        redis_instance_mock.set.assert_called_once_with('key', json.dumps(value), 'ttl')

    @mock.patch('healthyiocache.redis.cache.Redis')
    def test_delete(self, cache_client_mock):
        redis_instance_mock = mock.Mock()
        cache_client_mock.return_value = redis_instance_mock
        cache = Cache({'host': 'host', 'port': 'port', 'ttl': 'ttl'})
        cache_client_mock.assert_called_once_with(host='host', port='port')

        cache.put('key', {'value': 'value'})
        cache.delete('key')

        redis_instance_mock.delete.assert_called_once_with('key')
