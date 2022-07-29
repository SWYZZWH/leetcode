# You are asked to design a file system that allows you to create new paths and associate them with different values.
#
# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.
#
# Implement the FileSystem class:
#
# bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
# int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.

# Constraints:
#
# The number of calls to the two functions is less than or equal to 104 in total.
# 2 <= path.length <= 100
# 1 <= value <= 109

class FileSystem:
    class PathNode:
        def __init__(self, val: int):
            self.val = val
            self.children = {}

        def add_child(self, path: str, node):
            self.children[path] = node

        def child_exist(self, path: str) -> bool:
            return path in self.children

        def get_child(self, path: str):
            return self.children[path] if path in self.children else None

    # Trie Based or Dict Based
    def __init__(self):
        self.root = self.PathNode(-1)

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")
        p = self.root
        for i in range(1, len(paths) - 1):
            if p is None or not p.child_exist(paths[i]):
                return False
            p = p.get_child(paths[i])
        if p.child_exist(paths[-1]):
            return False
        p.add_child(paths[-1], self.PathNode(value))
        return True

    def get(self, path: str) -> int:
        paths = path.split("/")
        p = self.root
        for i in range(1, len(paths) - 1):
            if p is None or not p.child_exist(paths[i]):
                return -1
            p = p.get_child(paths[i])
        if p is None or p.get_child(paths[-1]) is None:
            return -1
        return p.get_child(paths[-1]).val