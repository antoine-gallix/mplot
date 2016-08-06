from copy import deepcopy


class CircularList():
    """a circular list can be indexed with values superior to its length, it just wraps
    """

    def __init__(self, from_list=None):
        if not from_list:
            from_list = []
        self._list = deepcopy(from_list)

    def __eq__(self, l):
        """compares to the internal list
        """
        return l == self._list

    def __getitem__(self, i):
        return self._list[i % len(self._list)]

    def enumerate(self):
        return enumerate(self._list)
