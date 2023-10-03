class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            if max_wealth < sum(account):
                max_wealth = sum(account)
        return max_wealth