from abc import ABC, abstractmethod
from dataclasses import dataclass


class Node(ABC):
    """A base class for nodes in the regular expression tree."""
    next: 'Node' = None
    consumes: int = 0

    @dataclass
    class TestResult:
        """A class to hold the results of a test operation."""
        matched: bool
        offset: int

    @abstractmethod
    def test(self, index: int, string: str, limit: int) -> TestResult:
        """Test if the node matches the string at the given index."""

    @abstractmethod
    def __repr__(self):
        """Return a string representation of the node."""


class CharNode(Node):
    """A node that matches a single character."""

    def __init__(self, char):
        self.char = char
        self.consumes = 1

    def __repr__(self):
        return f'|{self.char}|'

    def test(self, index: int, string: str, limit: int) -> Node.TestResult:
        if index >= len(string) or index >= limit:
            return Node.TestResult(False, 0)

        if string[index] == self.char:
            return Node.TestResult(True, 1)

        return Node.TestResult(False, 0)


class ControlNode(Node):
    """A node that matches a control character."""

    def __init__(self, control):
        self.control = control
        self.consumes = 0
        if control == '.':
            self.consumes = 1

    def __repr__(self):
        return f'[{self.control})]'

    def test(self, index: int, string: str, limit: int) -> Node.TestResult:
        if index >= len(string) and self.control != '$':
            return Node.TestResult(False, 0)

        match self.control:
            case '.':
                return Node.TestResult(True, 1)
            case '^':
                return Node.TestResult(index == 0, 0)
            case '$':
                return Node.TestResult(index == len(string), 0)


class RepeatingNode(Node):
    """A node that matches a repeating character."""

    def __init__(self, node, ntype):
        self.node = node
        self.type = ntype
        self.consumes = 0

    def __repr__(self):
        return f'R({self.node}, {self.type})'

    def test(self, index: int, string: str, limit: int) -> Node.TestResult:
        if index >= len(string):
            return Node.TestResult(False, 0)
        if self.type == '?':
            if self.node.test(index, string, limit).matched:
                return Node.TestResult(True, 1)
            return Node.TestResult(True, 0)

        if self.type == '*':
            offset = 0
            while index + offset < limit:
                result = self.node.test(index + offset, string, limit)
                offset += result.offset
                if not result.matched:
                    break
            return Node.TestResult(True, offset)
        if self.type == '+':
            offset = 0
            while index + offset < limit:
                result = self.node.test(index + offset, string, limit)
                offset += result.offset
                if not result.matched:
                    break
            return Node.TestResult(offset > 0, offset)

        return Node.TestResult(False, 0)


@dataclass
class MyFound:
    """A class to hold the results of a find operation."""
    span: tuple[int, int]
    matched: str


class MyRegex:
    """A class to hold a regular expression."""

    def __init__(self, pattern):
        """Create a new regular expression."""
        self.pattern = pattern
        self.nodes = self.__parse_nodes()

    def find(self, string: str) -> MyFound:
        """Find the first match in the given string."""
        for match in self.find_all(string):
            return match
        return None

    def __parse_nodes(self):
        nodes = []
        escape = False
        for symbol in self.pattern:
            if symbol in ('.', '^', '$') and not escape:
                nodes.append(ControlNode(symbol))
            elif symbol in ('?', '*', '+') and not escape:
                nodes.append(RepeatingNode(nodes.pop(), symbol))
            elif '\\' == symbol and not escape:
                escape = True
            else:
                nodes.append(CharNode(symbol))
                escape = False

        return nodes

    def find_all(self, string: str):
        """Find all matches in the given string."""
        if not self.nodes and not string:
            yield MyFound((0, 0), '')
            return

        if not string:
            return
        start = 0
        index = 0
        while index < len(string):
            start = index
            moved = False
            for node_index, node in enumerate(self.nodes):
                consuming = sum(map(lambda node: node.consumes,
                                self.nodes[node_index+1:]))
                limit = len(string) - consuming
                result = node.test(index, string, limit)
                if not result.matched:
                    break
                index += result.offset
                if result.offset > 0:
                    moved = True
            else:
                yield MyFound((start, index), string[start:index])
            if not moved:
                index += 1