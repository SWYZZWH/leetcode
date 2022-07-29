from unittest import TestCase

from no_472 import Solution


class TestSolution(TestCase):
    def test_find_all_concatenated_words_in_adict(self):
        s = Solution()
        self.assertEqual(["catsdogcats", "dogcatsdog", "ratcatdogcat"], s.findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
