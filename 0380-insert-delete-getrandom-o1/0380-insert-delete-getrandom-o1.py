class RandomizedSet:

    def __init__(self):
        self.idx_map = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        
        self.idx_map[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False

        idx_to_remove = self.idx_map[val]
        last_element = self.elements[-1]
        
        self.elements[idx_to_remove] = last_element
        self.idx_map[last_element] = idx_to_remove

        del self.idx_map[val]
        self.elements.pop()
        return True

    def getRandom(self) -> int:
        if not self.elements:
            return None
        idx = randint(0, len(self.elements) - 1)
        return self.elements[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()