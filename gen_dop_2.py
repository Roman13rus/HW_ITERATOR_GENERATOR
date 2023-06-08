import types
def list_unpacker(nest_list): # распаковщик списков
    nested = True
    while nested:
        new = []
        nested = False
        for i in nest_list:
            if isinstance(i, list):
                new.extend(i)
                nested = True
            else:
                new.append(i)
        nest_list = new
    return nest_list

def flat_generator(list_of_list):
    for item in list_unpacker(list_of_list):
        yield item
   
def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()