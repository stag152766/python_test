from sys import maxsize

class Contact:
    def __init__(self, first=None, middle=None, last=None, id = None):
        self.first = first
        self.middle = middle
        self.last = last
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id)

    def __eq__(self, other):
        return (self.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
