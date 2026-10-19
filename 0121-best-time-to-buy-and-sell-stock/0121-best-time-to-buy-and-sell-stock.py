class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_profit = float("inf")
        


        n = len(prices)
        for i in range(0,n):
            min_profit = min(min_profit, prices[i])

            max_profit = max(max_profit, prices[i] - min_profit)

        return max_profit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna