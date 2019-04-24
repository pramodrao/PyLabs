class IntSet(object):
    """Set of Integers"""
    def __init__(self):
        """Create an empty set of Integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer. True if e is present else False"""
        return e in self.vals

    def remove(self, e):
        """Removes the element from self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) +'not found!!')

    def getMembers(self):
        """Returns a list containing the elements in the self"""
        return self.vals[:]

    def __str__(self):
        """String representation"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'
