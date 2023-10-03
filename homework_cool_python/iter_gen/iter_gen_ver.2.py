import types


def flat_generator(list_of_lists: list):

    counter = 0
    sec_counter = 0
    while counter < len(list_of_lists):
        while sec_counter < len(list_of_lists[counter]):
            yield list_of_lists[counter][sec_counter]
            sec_counter += 1
            if sec_counter == len(list_of_lists[counter]):
                sec_counter = 0
                break
        counter += 1
        if counter == len(list_of_lists):
            break


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == \
           ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    if test_2() is None:
        print('Всё окау!')
