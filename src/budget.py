"""Small expense calculator for the A9 educational lab."""


def total_expenses(amounts):
    total = 0
    for amount in amounts:
        total += amount
    return total


def remaining_budget(limit, amounts):
    return limit - total_expenses(amounts)
