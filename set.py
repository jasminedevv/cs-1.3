from hashtable import HashTable

class Set(HashTable):
    def __init__(self, data=None):
        
        if data == None:
            super().__init__()

        elif type(data) != list:
            super().__init__()
            self.add(data)
        else:
            size = len(data)
            super().__init__(size*2)
            for item in data:
                self.add(item)

    def add(self, item):
        self.set(item, 0) # we only need the key so set value to 0

    def remove(self, item):
        self.delete(item)

    def union(self, other_set):
        new_set = Set(self.keys() + other_set.keys())
        return new_set

    def difference(self, other_set):
        difference = Set()
        
        for item in other_set.keys():
            if not self.contains(item):
                difference.add(item)

        for item in self.keys():
            if not other_set.contains(item):
                difference.add(item)
        return difference

    def intersection(self, other_set):
        intersection = Set()
        for item in self.keys():
            if other_set.contains(item):
                intersection.add(item)
        return intersection

    def is_subset(self, other_set):
        """Check if this set is a subset of another set"""
        for item in self.keys():
            if not other_set.contains(item):
                return False
        return True

