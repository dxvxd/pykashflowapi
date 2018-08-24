from collections import UserDict


class KfObject(UserDict):
    _items = {}

    def __setitem__(self, key, item):
        if key not in self._items.keys():
            raise KeyError('Key not defined')
        if not isinstance(item, self._items.get(key)):
            raise ValueError('Not right type of value. Need {}, but got {}'.format(self._items[key], type(item)))
        super().__setitem__(key, item)
