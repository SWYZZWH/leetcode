from unittest import TestCase

from no_432 import AllOne

class TestNode(TestCase):

    def test(self):
        s = AllOne()
        print(s.inc("hello"))
        print(s.inc("good"))
        print(s.inc("hello"))
        print(s.inc("hello"))
        print(s.getMaxKey())
        print(s.inc("leet"))
        print(s.inc("code"))
        print(s.inc("leet"))
        print(s.dec("hello"))
        print(s.inc("leet"))
        print(s.inc("code"))
        print(s.inc("code"))
        print(s.getMaxKey())

# ["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
# [[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]