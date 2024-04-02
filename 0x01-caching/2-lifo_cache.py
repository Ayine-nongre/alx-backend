#!/usr/bin/env python3
""" Last in first out tasks """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache """
    