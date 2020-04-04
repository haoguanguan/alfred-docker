# -*- coding: UTF-8 -*-

"""
@author:
haoguanguan

@usage:
format the result as alfred struct
"""

import abc
import json
from dicttoxml import dicttoxml


class Item(object):
    def __init__ (self, arg=None, title=None, subtitle=None, icon_path=None):
        self.arg = arg
        self.subtitle = subtitle
        self.icon = icon_path
        self.title = title

    def _handle_key(self, k):
        if k == "icon":
            return {"path": self.__dict__[k]}

        return self.__dict__[k]

    def to_map(self):
        return {k : self._handle_key(k) for k in self.__dict__ if self.__dict__[k]}


class AlfredClass(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.items = list()

    def push_back(self, item):
        self.items.append(item.to_map())
        return self

    @abc.abstractmethod
    def dump(self):
        pass


class AlfredXml(AlfredClass):
    def dump(self):
        return dicttoxml({"items": self.items}, attr_type=False, root=False)


class AlfredJson(AlfredClass):
    def dump(self):
        return json.dumps({"items": self.items})
