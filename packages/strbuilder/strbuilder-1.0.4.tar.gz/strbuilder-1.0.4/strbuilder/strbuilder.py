import typing as t
import types


class IWritable(list):
    def build(self) -> str:
        pass

    def write(self, code: 'Writable'):
        if isinstance(code, str):
            if code == '':
                return self
            self.append(code)
        elif isinstance(code, IWritable):
            self.write(code.build())
        elif isinstance(code, (list, tuple, map, filter, set)):
            self.extend(code)
        elif isinstance(code, types.GeneratorType):
            for item in code:
                self.write(item)
        elif callable(code):
            self.write(code())
        else:
            self.append(str(code))
        return self

    def write_if(self, condition: bool, code: 'Writable', or_else: t.Optional['Writable'] = None):
        if condition:
            self.write(code)
        elif or_else is not None:
            self.write(or_else)
        return self

    codes: t.List['Writable']


Writable = t.Union[str, IWritable, t.Any]


class Builder(IWritable):
    def __init__(self, *base: str, separator: t.Optional[str] = ' ') -> None:
        self.write(base)
        self.separator: str = separator

    def build(self):
        return self.separator.join(self)


class SurroundBuilder(IWritable):
    def __init__(self, *base: str, surround: t.Optional[t.List[str]] = '""', separator: t.Optional[t.Union[str, t.List]] = '') -> None:
        self.surround = surround
        self.separator = separator
        self.write(base)

    def build(self) -> str:
        return f'{self.surround[0]}{self.separator.join(self)}{self.surround[1]}'
