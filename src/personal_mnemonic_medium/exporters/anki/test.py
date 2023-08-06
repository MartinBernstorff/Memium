from typing import Any, Callable, Iterable, Iterator


class DotableIter:
    def __init__(self, iterable: Iterable[Any]):
        self.iterable = iter(iterable)

    def filter(self, func: Callable[..., Any]):
        processed = filter(func, self.iterable)
        return DotableIter(processed)

    def map(self, func: Callable[..., Any]):
        processed = map(func, self.iterable)
        return DotableIter(processed)

    def __iter__(self):
        return self.iterable

    def collect(self):
        return list(self.iterable)


itera = DotableIter(test).filter(lambda x: x > 2).map(lambda x: x * 2).collect()
iterb = [x * 2 for x in test if x > 2]
iterc = list(map(lambda x: x * 2, filter(lambda x: x > 2, test)))
print(itera)
