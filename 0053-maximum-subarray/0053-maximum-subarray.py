class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxi = float("-inf")
        total = 0
        for i in range(0 , n):
            total = total + nums[i]
            maxi = max(maxi, total)
            if total < 0 :
                total = 0
        return maxi        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna