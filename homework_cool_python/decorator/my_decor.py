from my_decor_decoration import logger


class FlatIterator:

    def __init__(self, list_of_list: list):

        self.lists = list_of_list

    def __iter__(self):

        self.counter = 0
        self.sec_counter = 0
        return self

    def __next__(self):

        while self.counter < len(self.lists):
            while self.sec_counter < len(self.lists[self.counter]):
                item = self.lists[self.counter][self.sec_counter]
                self.sec_counter += 1
                return item
            self.sec_counter = 0
            self.counter += 1
        raise StopIteration


@logger()
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == \
           ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    if test_1() is None:
        print('Всё окау!')
