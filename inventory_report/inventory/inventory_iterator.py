from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def _get_element_by_index(self, index):
        return self.data[index]

    def __next__(self):
        data = self._get_element_by_index(index=self.index)

        if not data:
            raise StopIteration()

        self.index += 1
        return data
