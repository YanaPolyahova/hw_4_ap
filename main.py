from itertools import chain


class FIterator:
    def __init__(self, any_list):
        self.list = iter(chain(*any_list))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.list)


def flat_generator(any_list):
    a_list = list(chain(*any_list))
    while a_list:
        yield a_list[0]
        a_list.pop(0)


if __name__ == '__main__':

    nested_list = [['a', 'b', 'c'],
                   ['d', 'e', 'f', 'h', False],
                   [1, 2, None],
                   ]

    for item in FIterator(nested_list):
        print(item)
    result = [item for item in FIterator(nested_list)]
    print(result)
    for item in flat_generator(nested_list):
        print(item)
