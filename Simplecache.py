"""
Title: simplecache
Author: Harold Goldman
Date: 10/15/2017
URL: https://github.com/mikerah13/Simplecache
email: mikerah@gmail.com
Description:
    Simple Cache object
"""
from __future__ import print_function
from sys import getsizeof
from collections import OrderedDict
from time import time
import json


class Simplecache(object):
    """
    simple cache object
    """

    def __init__(self):
        """
        init
        args:
            self
        vars:
            nothing
        returns:
            nothing
        raises:
            nothing
        """
        self.__cache = OrderedDict()
        self.__max_size = 1000000
        self.__ttl = False

    def __expire(self):
        """
        remove keys, vals with expired ttl's
        args:
            self
        vars:
            nothing
        returns:
            nothing
        raises:
            exception
        """
        try:
            for key, value in self.__cache.iteritems():
                if value["time"] < time():
                    self.delete(key)
        except:
            raise

    def __value(self, val):
        """
        create value for cache
        args:
            self
            val
        vars:
            nothing
        returns:
            value
        raises:
            nothing
        """
        return ({"val": val, "time": time() + self.__ttl})

    def timeleft(self, key):
        """
        seconds till expired
        args:
            self
            key
        vars:
            nothing
        returns:
            time left in seconds / False
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            if self.incache(key):
                return int(self.__cache[key]["time"] - time())
            return False
        except:
            raise

    def setttl(self, ttl):
        """
        set ttl
        args:
            self
            ttl <int>
        vars:
            nothing
        returns:
            nothing
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            self.__ttl = ttl
        except:
            raise

    def getttl(self):
        """
        get ttl
        args:
            self
        vars:
            nothing
        returns:
            self.ttl
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return self.__ttl
        except:
            raise

    def setmax(self, size):
        """
        set max size
        args:
            self
            size <int>
        vars:
            nothing
        returns:
            nothing
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            self.__max_size = size
        except:
            raise

    def getmax(self):
        """
        get max size
        args:
            self
        vars:
            nothing
        returns:
            self.max_size <int>
        raises:
            nothing
        """
        try:
            if self.__ttl:
                self.__expire()
            return self.__max_size
        except:
            raise

    def insert(self, key, item):
        """
        insert into cache
        args:
           self
           key
           item
        vars:
           none
        returns:
           True
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            if self.length() == self.__max_size:
                self.pop()
                self.__cache[key] = self.__value(item)
            else:
                self.__cache[key] = self.__value(item)
        except ValueError:
            raise
        except:
            raise

    def incache(self, key):
        """
        search cache for key
        args:
            self
            key
        vars:
            none
        returns:
            True/False
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return key in self.__cache
        except ValueError:
            raise
        except:
            raise

    def search(self, key):
        """
        search cache for value
        args:
            self
            key
        vars:
            none
        returns:
            self.cache[key]/False
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return self.__cache[key]["val"]
        except KeyError:
            return False
        except ValueError:
            raise
        except:
            raise

    def delete(self, key):
        """
        delete from cache
        args:
            self
            key
        vars:
            none
        returns:
            True/ False
        raises:
            exception
        """
        try:
            return self.__cache.pop(key, None)
        except ValueError:
            raise
        except:
            raise

    def pop(self):
        """
        pop (remove oldest)
        args:
            self
        vars:
            none
        returns:
            True/False
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            self.__cache.popitem(last=False)
        except ValueError:
            raise
        except:
            raise

    def oldest(self):
        """
        return oldest entry
        args:
            self
        vars:
            none
        returns:
            none
        raises:
            ValueError/unhandled exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return self.__cache.keys()[0]
        except ValueError:
            raise
        except:
            raise

    def youngest(self):
        """
        return youngest entry
        args:
            self
        vars:
            none
        returns:
            none
        raises:
            ValueError/unhandled exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return self.__cache.keys()[-1]
        except ValueError:
            raise
        except:
            raise

    def print(self):
        """
        print the contents of the cache
        args:
            self
        vars:
            none
        returns:
            none
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            data = OrderedDict()
            for key, value in self.__cache.iteritems():
                data[key] = value["val"]
            print(json.dumps(data, indent=1))
        except ValueError:
            raise
        except:
            raise

    def length(self):
        """
        get length of cache
        args:
            self
        vars:
            none
        returns:
            length <int>
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return len(self.__cache)
        except ValueError:
            raise
        except:
            raise

    def size(self):
        """
        get size of cache
        args:
            self
        vars:
            none
        returns:
            size <int>
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            return getsizeof(self.__cache)
        except ValueError:
            raise
        except:
            raise

    def limit(self):
        """
        limit cache to max_size
        args:
            self
        vars:
            none
        returns:
            None
        raises:
            exception
        """
        try:
            if self.__ttl:
                self.__expire()
            while self.length() > self.__max_size:
                self.__cache.popitem(last=False)
        except ValueError:
            raise
        except:
            raise

    def write(self, target):
        """
        write cache to json file
        args:
            self
            target <str>
        vars:
            none
        returns:
            none
        raises:
            unhandled exception
        """
        try:
            if self.__ttl:
                self.__expire()
            data = OrderedDict()
            for key, value in self.__cache.iteritems():
                data[key] = value["val"]
            with open(target, 'w') as outfile:
                json.dump(data, outfile)
        except IOError:
            raise
        except:
            raise

    def read(self, target):
        """
        read cache from json file
        args:
            self
            target <str>
        vars:
            none
        returns:
            none
        raises:
            unhandled exception
        """
        try:
            if self.__ttl:
                self.__expire()
            with open(target, 'r') as infile:
                data = (json.load(infile))
            for key, value in data.iteritems():
                self.insert(key, value)
        except IOError:
            raise
        except:
            raise

    def clear(self):
        """
        clear the cache
        args:
            self
        vars:
            none
        returns:
            none
        raises:
            unhandled exception
        """
        try:
            self.__init__()
        except:
            raise

    def merge(self, target):
        """
        merged target Simplecache with self
        args:
            self
            target
        vars:
            none
        returns:
            none
        raises:
            unhandled exception
        """
        try:
            if self.__ttl:
                self.__expire()
            temp_max = self.__max_size
            self.unload(target)
            self.clear()
            self.__max_size = temp_max
            self.load(target)
        except:
            raise

    def load(self, target):
        """
        loads target dictionary items into self
        args:
            self
            target
        vars:
            none
        returns:
            none
        raises:
            unhandled exception
        """
        try:
            if self.__ttl:
                self.__expire()
            for key, value in target.iteritems():
                self.__cache[key] = self.__value(value)
        except:
            raise

    def unload(self, target):
        '''
        unloads self into target dictionary
        args:
            self
            target
        vars:
            none
        returns:
            none
        raises:
            unhandled exception
        '''
        try:
            if self.__ttl:
                self.__expire()
            for key, value in self.__cache.iteritems():
                target[key] = value
        except:
            raise
