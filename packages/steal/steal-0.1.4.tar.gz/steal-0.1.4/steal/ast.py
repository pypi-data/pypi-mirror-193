from typing import TypeVar, Generic, List, Generator
from dataclasses import dataclass, field
from steal.langspec import opcodes
from steal.scanner import TokenType, Token

class CompilerError(Exception):
    
    def __init__(self, msg, **kwargs):
        self.token = kwargs.get('token')
        super().__init__('{} (Token = {})'.format(msg, self.token))

T = TypeVar('T')
@dataclass
class Node(Generic[T]):

    value: str
    is_label: bool = False
    immediate_args: List[str] = field(default_factory=lambda: [])
    children: List = field(default_factory=lambda: [])

    @classmethod
    def from_tokens(cls, tokens: Generator[Token, None, None], head: Token = None) -> T:
        token = head or next(tokens)
        if token.token_type == TokenType.BEGIN:
            node = Node.from_tokens(tokens)
            token = next(tokens)
            while token.token_type != TokenType.END:
                child = Node.from_tokens(tokens, head=token)
                node.children.append(child)
                token = next(tokens)

            if not node.is_label:
                try:
                    opcode = opcodes[node.value]
                except KeyError:
                    raise CompilerError('Invalid opcode', token=token)

                # This should be verified
                # if len(node.immediate_args) != opcode.size - 1:
                #     raise CompilerError('Invalid immediate args', token=token)

                # if len(node.children) != len(opcode.arg_types):
                #     raise CompilerError('Invalid stack args', token=token)

            if token.token_type != TokenType.END:
                raise CompilerError('Unclosed expression', token=token)

            return node
        elif token.token_type == TokenType.BYTE:
            return Node(token.token_type.value,
                        immediate_args=['"%s"' % token.value])
        elif token.token_type == TokenType.INT:
            return Node(token.token_type.value,
                        immediate_args=[token.value])
        elif token.token_type in (TokenType.ATOM, TokenType.LABEL):
            immediate_args = token.value.split('.')
            value = immediate_args.pop(0)
            return Node(value,
                        immediate_args=immediate_args,
                        is_label=token.token_type == TokenType.LABEL)

        raise CompilerError('Invalid token', token=token)

    def __repr__(self) -> str:
        lines = []
        if self.is_label:
            lines.append(self.value)
        lines.extend([str(child) for child in self.children])
        if not self.is_label:
            lines.append(' '.join([self.value, *self.immediate_args]))
        return '\n'.join(lines)
