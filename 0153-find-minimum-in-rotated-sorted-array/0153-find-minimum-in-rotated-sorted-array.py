class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        minimum = float("inf")
        while low <= high :
            mid = (low + high)// 2

            if nums[mid] <= nums[high]:
                minimum = min(minimum ,nums[mid])
                high = mid - 1
            else:
                mini = (minimum, nums[low])
                low = mid + 1
        return minimum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna