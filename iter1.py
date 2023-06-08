class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cur = 0
        self.cur_vn = 0
        return self

    def __next__(self):
        if self.cur_vn <= len(self.list_of_list[self.cur]) - 1:
            items =  self.list_of_list[self.cur][self.cur_vn]
            self.cur_vn += 1
            return items
        else:
            self.cur_vn = 0
            self.cur += 1
            if self.cur < len(self.list_of_list):
                items =  self.list_of_list[self.cur][self.cur_vn]
                self.cur_vn = 1
                return items
            else:
                raise StopIteration
 
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

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()