from unittest import TestCase

from data_structure.DLinkedList.dlinked import DLinkedList, DLinkedNode


class TestDLinkedList(TestCase):
    def test(self):
        lst = DLinkedList()
        node_1 = DLinkedNode(1)
        node_2 = DLinkedNode(2)
        node_3 = DLinkedNode(3)
        lst.append(node_1)
        print(lst)
        lst.pop(node_1)
        print(lst)
        lst.append(node_1)
        print(lst)
        lst.append(node_2)
        print(lst)
        lst.append(node_3)
        print(lst)
        lst.popleft()
        print(lst)
        lst.popright()
        print(lst)
        lst.pop(node_2)
        print(lst)
