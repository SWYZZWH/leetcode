import collections
from typing import List


class Solution:
    # class Node:
    #     def __init__(self, val: str, next):
    #         self.val = val
    #         self.next = next
    #
    # class linked_map:
    #     def __init__(self, vals: List[str]):
    #         self.head = Node(-1, None)
    #         self.vals = {}
    #         p = self.head
    #         for val in vals:
    #             new_node = Node(val, None)
    #             assert val not in self.vals
    #             self.vals[val] = new_node
    #             p.next = new_node
    #             p = p.next
    #
    #     def add_after(self, before: str, val: str):
    #         assert before in self.vals and val not in self.vals
    #         before_node = self.vals[before]
    #         old_next = before_node.next
    #         new_node = Node(val, old_next)
    #         before_node.next = new_node
    #         self.vals[val] = new_node
    #
    #     def merge_with(self, m: "linked_map") -> "linked_map":
    #         if len(m.vals) > len(self.vals):
    #             return m.merge_with(self)
    #
    #         has_common = False
    #         for val in m.vals.keys():
    #             if val in self.vals:
    #                 has_common = True
    #                 m

    # self.all_ranges = []
    # self.hash =

    # def rec(self, words: List[str]) -> bool:
    #     cur_alpha = ""
    #     next_words = []
    #     words.append("-")
    #     for i, word in enumerate(words):
    #         if len(word) == 0:
    #             continue
    #         if cur_alpha != word[0] or word == "-":
    #             if len(next_words) != 0 and len(next_words) != 1:
    #                 if not self.rec(next_words):
    #                     return False
    #                 next_words = []
    #             if cur_alpha != "" and word != "-":
    #                 # new relation found: cur_alpha < word[0]
    #                 if cur_alpha not in self.rules:
    #                     self.rules[cur_alpha] = set(), {word[0]}
    #                 else:
    #                     if word[0] in self.rules[cur_alpha][0]:
    #                         return False
    #                     for small in self.rules[cur_alpha][0]:
    #                         self.rules[small][1].add(word[0])
    #                     self.rules[cur_alpha][1].add(word[0])
    #                 if word[0] not in self.rules:
    #                     self.rules[word[0]] = {cur_alpha}, set()
    #                 else:
    #                     if cur_alpha in self.rules[word[0]][1]:
    #                         return False
    #                     for large in self.rules[word[0]][1]:
    #                         self.rules[large][0].add(cur_alpha)
    #                     self.rules[word[0]][0].add(cur_alpha)
    #             cur_alpha = word[0]
    #
    #         # the new one
    #         next_words.append(word[1:])
    #
    #     return True
    #
    # # list and hash map
    # def alienOrder(self, words: List[str]) -> str:
    #     self.rules = {}
    #     if not self.rec(words):
    #         return ""
    #     cur_max = 0
    #     ret = ""
    #     for alpha, rule in self.rules.items():
    #         if len(rule[0]) + len(rule[1]) > cur_max:
    #             cur_max = len(rule[0]) + len(rule[1])
    #             ret = "".join(rule[0]) + alpha + "".join(rule[1])
    #     return ret

    # just try to give topology order of letters, only thing to notice: "abc", "ab" is invalid
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: Put all unique letters into the adj list.
        in_degree = {c: 0 for word in words for c in word}
        adj_list = collections.defaultdict(set)

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    in_degree[d] += 1
                    adj_list[c].add(d)
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # DFS approach by coloring
        # Step 2: Depth-first search.
        # seen = {}  # False = grey, True = black.
        # output = []
        #
        # def visit(node):  # Return True iff there are no cycles.
        #     if node in seen:
        #         return seen[node]  # If this node was grey (False), a cycle was detected.
        #     seen[node] = False  # Mark node as grey.
        #     for next_node in reverse_adj_list[node]:
        #         result = visit(next_node)
        #         if not result:
        #             return False  # Cycle was detected lower down.
        #     seen[node] = True  # Mark node as black.
        #     output.append(node)
        #     return True

        # if not all(visit(node) for node in reverse_adj_list):
        #     return ""

        # BFS approach:
        output = []
        nodes = collections.deque([c for c in in_degree if in_degree[c] == 0])
        while nodes:
            n = nodes.popleft()
            output.append(n)
            for adj in adj_list[n]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    nodes.append(adj)

        if len(output) < len(in_degree):
            return ""

        return "".join(output)
