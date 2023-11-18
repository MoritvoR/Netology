class Stack:
    def __init__(self, data=''):
        self.data = data
        self.len = len(self.data)

    def __str__(self):
        return self.data[::-1]

    def is_empty(self) -> bool:
        if self.len == 0:
            return True
        else:
            return False

    def push(self, new_elem: str) -> None:
        self.data += new_elem
        return None

    def pop(self) -> str:
        element = self.data[-1]
        self.data = self.data[:-1]
        return element

    def peek(self) -> str:
        element = self.data[-1]
        return element

    def size(self) -> int:
        return self.len
