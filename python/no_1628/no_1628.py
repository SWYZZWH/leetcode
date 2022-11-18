import abc
from abc import ABC, abstractmethod
from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

# python class design
# abstract class
# class and subclass

class Node(ABC):

    @abstractmethod
    def evaluate(self) -> int:
        pass


class NumberNode(Node):

    def __init__(self, val: int):
        self.val = val

    def evaluate(self) -> int:
        return self.val


class OpNode(Node):

    def __init__(self, left: "Node", right: "Node"):
        self.left = left
        self.right = right


class DivNode(OpNode):

    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()


class MulNode(OpNode):

    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()


class AddNode(OpNode):

    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class SubNode(OpNode):

    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':

        def rec(i: int) -> ('Node', int):
            if postfix[i][0].isdigit():
                return NumberNode(int(postfix[i])), i - 1

            r, r_idx = rec(i - 1)
            l, l_idx = rec(r_idx)

            cur = None
            if postfix[i] == "+":
                cur = AddNode(l, r)
            elif postfix[i] == "-":
                cur = SubNode(l, r)
            elif postfix[i] == "*":
                cur = MulNode(l, r)
            else:
                cur = DivNode(l, r)
            return cur, l_idx

        return rec(len(postfix) - 1)[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
