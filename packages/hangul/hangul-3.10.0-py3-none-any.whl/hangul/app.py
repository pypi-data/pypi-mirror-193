from collections.abc import Generator, Iterable, Iterator
from io import StringIO
from itertools import islice
from typing import Any, List, Tuple

import json
import os


class Iteration:

    @staticmethod
    def chunks(iterable: Iterable[Any], n: int) -> Iterator[List[str]]:
        """
        Split a list into n-sublist.
        Example: chunks([1, 2, 3, 4, 5], 2) -> [1, 2] [3, 4] [5]
        """
        def _w(g, n):
            return lambda: tuple(islice(g, n))
        return iter(_w(iter(iterable), n), ())


class Hangul:

    """
    The official Korean language romanization system in Python.
    """

    @property
    def __data(self):
        path = os.path.dirname(__file__)
        with open(f'{path}/static/data.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def __unpack(self, s: str) -> Generator[Tuple[str]]:
        for i in range(len(s)):
            if i not in [0, len(s) - 1]:
                yield self.jamo(s[i])
            else:
                if i == 0:
                    # first character: prepend one empty string
                    yield ('', *self.jamo(s[i]))
                else:
                    # last character: append two empty strings
                    yield (*self.jamo(s[i]), '', '')

    def jamo(self, s: str) -> Tuple[str]:
        """
        Transform a unicode character to its containing positional form.
        Example: jamo('사') -> ('ᄉ', 'ᅡ', '')
        """
        #! warning: do not alter this algorithm
        if 44032 <= (x := ord(s)) <= 55203:
            a = x - 44032
            b = a % 28
            c = 1 + ((a - b) % 588) // 28
            d = 1 + a // 588
            q = [*map(sum, zip(*[[d, c, b], [4351, 4448, 4519]]))]
            if b:
                return (chr(q[0]), chr(q[1]), chr(q[2]))
            return (chr(q[0]), chr(q[1]), '')
        return ('', s, '')

    def romanize(self, s: str) -> StringIO:
        """
        Transcribes Korean characters into Latin alphabet.
        """
        if len(s) == 1:
            # IndexError is raised when the string contains one character
            return StringIO(s)
        output = StringIO()
        for i in Iteration.chunks((j for i in self.__unpack(s) for j in i), 3):
            try:
                output.write(self.__data[f"{i[0] or '-'}{i[1] or '-'}"])
            except KeyError:
                pass
            try:
                output.write(self.__data[f"-{i[2]}"])
            except KeyError:
                output.write(i[2])
        output.seek(0)
        return output


def romanize(s: str) -> str:
    """
    Transcribes Korean characters into Latin alphabet.
    """
    return Hangul().romanize(s).read()


if __name__ == '__main__':
    hangul = Hangul()
    print(hangul.jamo('를'))
    print(hangul.romanize('나는 TV를 사랑').read())
