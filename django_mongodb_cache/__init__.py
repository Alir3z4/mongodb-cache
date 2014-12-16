__version__ = (2014, 12, 16)
__author__ = "Jonas Haag <jonas@lophus.org>"

from backend import MongoDBCache

# Django < 1.3 compatibility
CacheClass = MongoDBCache
