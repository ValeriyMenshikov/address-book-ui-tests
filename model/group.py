from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return f"Name={self.name}, id={self.id}, Header={self.header}, Footer={self.footer}"

    def __eq__(self, other):
        return self.name == other.name and (self.id is None or other.id is None or self.id == other.id) \
               and self.header == other.header \
               and self.footer == other.footer

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
