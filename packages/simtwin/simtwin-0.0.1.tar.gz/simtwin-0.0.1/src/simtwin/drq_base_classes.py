"""
Contains base classes for simtwin objects
"""
from enum import Enum
from abc import ABC, abstractmethod


class DrqObjectBase(ABC):
    """
    Abstract base class for managed simtwin objects.
    """
    @abstractmethod
    def __serialize__(self):
        """
        Returns serialized bytes for the objects data
        """

    @abstractmethod
    def __deserialize__(self, data):
        """
        Updates the object with serialized input from data.
        """

    @abstractmethod
    def __eq__(self, other):
        pass

    def __pull__(self):
        """
        Updates the object from the remote server.
        """
        self._server.pull(self.obj_index)

    def __push__(self):
        """
        Pushes the current version of the object to the remote server.
        """
        self._server.push(self.obj_index)

    @property
    def refresh_stamp(self):
        """
        Returns an Integer representing the age of the data in the object.
        Newer objects will have a larger stamp
        """
        return self._refresh_stamp

    def __update_remote__(self):
        """
        updates the refresh stamp of the object and pushes it to the respective remote server
        """
        if self._server.is_remote_server:
            self._refresh_stamp += 1
            self.__push__()

    @property
    def up_to_date(self):
        """
        Returns true if the object is in sync with the client
        """
        stamp_at_server = self._server.get_refresh_stamp(self.obj_index)
        return stamp_at_server <= self._refresh_stamp

    @property
    def obj_index(self):
        """
        obj_index of the object
        """
        return self._obj_index

    @obj_index.setter
    def obj_index(self, obj_index):
        self._obj_index = obj_index
        self._refresh_stamp = -1

    def call_method(self, name, args={}):  # pylint: disable=W0102
        """
        Calls the method "name" within the corresponding server side object with the given keyword arguments
        """
        if self._server.is_remote_server:
            return self._server.call_method(name, self._obj_index, args)
        return self.methods[name](**args)

    def __init__(self, server=None, obj_index=None):
        if not hasattr(self, 'methods'):
            self.methods = {}
        self._server = server
        if obj_index is None:
            self._obj_index = server.add_obj(self)
            self._refresh_stamp = 0
            server.push(self.obj_index)
        else:
            self._obj_index = obj_index
            self._refresh_stamp = -1
            server.pull(self.obj_index)

    def __del__(self):
        self._server.remove(self.obj_index)


class DrqEnum(Enum):
    """
    Baseclass for enums in simtwin
    """
    def __serialize__(self):
        return self.value.to_bytes(8, 'little')
