"""Regression checks run on every Dependabot pull request."""
import unittest

from src.budget import remaining_budget, total_expenses


class BudgetTests(unittest.TestCase):
    def test_empty_expenses(self):
        self.assertEqual(total_expenses([]), 0)

    def test_multiple_expenses(self):
        self.assertEqual(total_expenses([100, 250, 50]), 400)

    def test_remaining_budget(self):
        self.assertEqual(remaining_budget(1000, [100, 250]), 650)

    def test_over_budget(self):
        self.assertEqual(remaining_budget(100, [150]), -50)


if __name__ == "__main__":
    unittest.main()
