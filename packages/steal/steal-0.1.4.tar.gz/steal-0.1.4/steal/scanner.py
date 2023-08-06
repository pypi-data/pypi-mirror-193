import sys
from enum import Enum
from typing import TextIO, Generator
from collections.abc import Callable


class TokenType(Enum):
    BEGIN = '('
    END = ')'
    BYTE = 'byte'
    INT = 'int'
    ATOM = 'atom'
    LABEL = 'label'

class Token:

    def __init__(self, token_type: TokenType, value: str = None, depth: int = 0):
        self.token_type = token_type
        self.value = value
    
    def __repr__(self):
        return '{}({})'.format(self.token_type.name, self.value)
    

def scan(f: TextIO) -> Generator[Token, None, None]:
    def consume(unless: Callable, c: str):
        value = ''
        while unless(c):
            value += c
            c = f.read(1)
        return c, value

    def atom_test(c):
        return c not in [TokenType.BEGIN.value, TokenType.END.value, '"']\
            and not c.isspace()

    c = f.read(1)
    while c:
        if c == TokenType.BEGIN.value:
            yield Token(TokenType.BEGIN)
            c = f.read(1)
        elif c == TokenType.END.value:
            yield Token(TokenType.END)
            c = f.read(1)
        elif c == '"':
            c, value = consume(lambda c: c != '"', f.read(1))
            yield Token(TokenType.BYTE, value)
            c = f.read(1)
        elif c.isnumeric():
            c, value = consume(lambda c: c.isnumeric(), c)
            yield Token(TokenType.INT, value)
        elif atom_test(c):
            c, value = consume(atom_test, c)
            if value.endswith(':'):
                yield Token(TokenType.LABEL, value)
            else:
                yield Token(TokenType.ATOM, value)
        else:
            c = f.read(1)

def main():
    with open(sys.argv[1]) as f:
        for token in scan(f):
            print(token)

if __name__ == '__main__':
    main()