"""
Title: test_cache.py
Author: Harold Goldman
Date: 10/11/2017
email: mikerah@gmail.com
Description:
    pytest tests for Simplecache
"""
from __future__ import print_function
import os
from Simplecache import Simplecache
import pytest


@pytest.fixture(scope="module")
def cache():
    """
    base fixture for Simplecache tests
    args:
        none
    vars:
        none
    returns:
        SimpleCache()
    raises:
        none
    """
    return Simplecache()


@pytest.fixture(scope="module")
def test_data():
    """
    data for testing Simplecache.Simplecache
    args:
        none
    vars:
        none
    returns:
        infile.read() <stream>
    raises:
        none
    """
    with open(r"test\data\test_data_input.json") as infile:
        return infile.read()


def test_init(cache):
    """
    test Simplecache.Simplecache.__init__()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    assert cache.max_size == 1000000


def test_max_size(cache):
    """
    test Simplecache.Simplecache.max_size
    """
    cache.clear()
    cache.max_size = 30
    assert cache.max_size == 30


def test_setmax(cache):
    """
    test Simplecache.Simplecache.setmax()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.setmax(5)
    assert cache.max_size == 5


def test_getmax(cache):
    """
    test Simplecache.Simplecache.getmax()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.setmax(100)
    assert cache.getmax() == 100


def test_insert(cache):
    """
    test Simplecache.Simplecache.insert()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.insert("test", "test data")
    assert cache.search("test") == "test data"


def test_incache(cache):
    """
    test Simplecache.Simplecache.incache()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.insert("incache", "data in cache")
    assert cache.incache("incache") is True


def test_search(cache):
    """
    test Simplecache.Simplecache.search()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.insert("a key", "a value")
    assert cache.search("a key") == "a value"


def test_delete(cache):
    """
    test Simplecache.Simplecache.delete()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.insert("delete key", "delete value")
    assert cache.search("delete key") == "delete value"
    cache.delete("delete key")
    assert cache.search("delete key") is False


def test_pop(cache):
    """
    test Simplecache.Simplecache.pop()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    cache.pop()
    cache.pop()
    assert cache.oldest() == 2


def test_oldest(cache):
    """
    test Simplecache.Simplecache.oldest()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    assert cache.oldest() == 0


def test_youngest(cache):
    """
    test Simplecache.Simplecache.youngest()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    assert cache.youngest() == 9


def test_print(cache, test_data, capsys):
    """
    test Simplecache.Simplecache.print()
    args:
        cache <Simplecache>
        test_data <stream>
        capsys <>
    vars:
        out <capsys.readouterr()>
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    cache.print()

    out = capsys.readouterr()
    print(out)
    assert str(out) == test_data


def test_length(cache):
    """
    test Simplecache.Simplecache.length()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    assert cache.length() == 10


def test_size(cache):
    """
    test Simplecache.Simplecache.size()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    assert cache.size() == 532


def test_limit(cache):
    """
    test Simplecache.Simplecache.limit()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    for item in range(10):
        cache.insert(item, item)
    cache.setmax(5)
    cache.limit()
    assert cache.length() == 5


def test_write(cache):
    """
    test Simplecache.Simplecache.write()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    try:
        os.remove(r"test\data\test_data_output.json")
    except IOError:
        pass
    except:
        pass
    for item in range(10):
        cache.insert(item, item)
    cache.write(r"test\data\test_data_output.json")
    with open(r"test\data\test_data_write.json") as infile:
        orig = infile.read()
    with open(r"test\data\test_data_output.json") as infile:
        new = infile.read()
    assert new == orig
    os.remove(r"test\data\test_data_output.json")


def test_read(cache):
    """
    test Simplecache.Simplecache.read()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.clear()
    cache.read(r"test\data\test_data_read.json")
    cache.print()
    assert cache.search("5") == 5


def test_clear(cache):
    """
    test Simplecache.Simplecache.clear()
    args:
        cache <Simplecache>
    vars:
        none
    returns:
        none
    raises:
        none
    """
    cache.read(r"test\data\test_data_read.json")
    cache.clear()
    assert cache.getmax() == 1000000
