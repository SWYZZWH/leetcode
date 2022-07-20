from unittest import TestCase

from no_1604 import Solution


class TestSolution(TestCase):
    def test_alert_names(self):
        s = Solution()
        self.assertEqual(["luis"], s.alertNames(["luis", "luis", "luis"], ["23:40", "23:50", "23:01"]))
        self.assertEqual(["clare","leslie"], s.alertNames(["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"], ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]))
