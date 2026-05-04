# "Given a list of transactions, find the user with highest average
# transaction value, excluding users with fewer than 5 transactions"

from collections import defaultdict
from typing import List, Dict, Optional

def find_top_user(transactions: List[Dict]) -> Optional[str]:
    """
    Find user with highest average transaction value.

    Args:
        transactions: List of dicts with 'user_id' and 'amount'

    Returns:
        user_id of top user, or None if no qualifying users
    """
    user_totals = defaultdict(lambda: {'sum': 0, 'count': 0})

    for txn in transactions:
        user_id = txn['user_id']
        user_totals[user_id]['sum'] += txn['amount']
        user_totals[user_id]['count'] += 1

    # Filter users with 5+ transactions and calculate averages
    qualifying_users = {
        user_id: data['sum'] / data['count']
        for user_id, data in user_totals.items()
        if data['count'] >= 5
    }

    if not qualifying_users:
        return None

    return max(qualifying_users, key=qualifying_users.get)