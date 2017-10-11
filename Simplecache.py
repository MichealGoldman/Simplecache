"""
Title: simplecache
Author: Harold Goldman
Date: 10/10/2017
email: mikerah@gmail.com
Description:
    Simple Cache object
"""
from __future__ import print_function
from sys import getsizeof
from collections import OrderedDict
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
        self.cache = OrderedDict()
        self.max_size = 1000000

    def setmax(self, size):
        """
        set max size
        args:
            self
            max <int>
        vars:
            nothing
        returns:
            nothing
        raises:
            nothing
        """
        self.max_size = size

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
        return self.max_size

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
            if self.length() == self.max_size:
                self.pop()
                self.cache[key] = item
            else:
                self.cache[key] = item
        except ValueError:
            raise
        except:
            raise

    def incache(self, key):
        """
        search cache
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
            return key in self.cache
        except ValueError:
            raise
        except:
            raise

    def search(self, key):
        """
        search cache
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
            return self.cache[key]
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
            return self.cache.pop(key)
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
            self.cache.popitem(last=False)
        except ValueError:
            raise
        except:
            raise

    def oldest(self):
        """
        return oldest entry
        """
        try:
            return self.cache.keys()[0]
        except ValueError:
            raise
        except:
            raise

    def youngest(self):
        """
        return youngest entry
        """
        try:
            return self.cache.keys()[-1]
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
            print(json.dumps(self.cache, indent=1))
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
            return len(self.cache)
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
            return getsizeof(self.cache)
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
            while self.length() > self.max_size:
                self.cache.popitem(last=False)
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
            with open(target, 'w') as outfile:
                json.dump(self.cache, outfile)
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
            with open(target, 'r') as infile:
                self.cache = (json.load(infile))
        except IOError:
            raise
        except:
            raise

    def clear(self):
        """
        clear the cache
        """
        try:
            self.__init__()
        except:
            raise
