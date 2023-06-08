class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_unpacker(list_of_list) # преобразуем список неопределенной вложенности в список без вложенности
    
    def __iter__(self):
        self.cur = 0
        return self

    def __next__(self):
        if self.cur <= len(self.list_of_list) - 1:
            items =  self.list_of_list[self.cur]
            self.cur += 1
            return items
        else:
            raise StopIteration
        
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

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()