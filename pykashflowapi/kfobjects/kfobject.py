from collections import UserDict


class KfObject(UserDict):
    _items = {}  # Required parameters that must be present in SOAP request
    _additional_items = {}  # Additional parameters - have them just to check existance on setting parameter

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, value in self._items.items():
            if self.get(key, None) is None:
                self[key] = value

    def __setitem__(self, key, item):
        if key not in self._items.keys() and key not in self._additional_items.keys():
            raise KeyError('Key not defined')
        if key in self._items.keys() and not isinstance(item, type(self._items.get(key))):
            raise ValueError('Not right type of value. Need {}, but got {}'.format(type(self._items[key]), type(item)))
        if key in self._additional_items.keys() and not isinstance(item, type(self._additional_items.get(key))):
            raise ValueError('Not right type of value. Need {}, but got {}'.format(
                type(self._additional_items[key]), type(item)))
        super().__setitem__(key, item)


