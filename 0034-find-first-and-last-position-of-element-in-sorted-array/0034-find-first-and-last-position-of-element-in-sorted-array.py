class Solution(object):

    def lowerbound(self, nums, target):
        n = len(nums)
        low = 0
        high = n

        lb = n

        while low < high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                lb = mid
                high = mid
            else:
                low = mid + 1

        return lb

    def upperbound(self, nums, target):
        n = len(nums)
        low = 0
        high = n

        ub = n

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ub = mid
                high = mid
            else:
                low = mid + 1

        return ub

    def searchRange(self, nums, target):
        lb = self.lowerbound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = self.upperbound(nums, target)

        return [lb, ub - 1]




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna