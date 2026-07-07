class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        richest_wealth=0   
        for customer in accounts:
            current_wealth = 0

            for accounts in customer :
                current_wealth += accounts

                if current_wealth > richest_wealth:
                    richest_wealth = current_wealth

        return  richest_wealth        
