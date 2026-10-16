class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for k, v in c.items():
            if c[k] > 1 :
                return True
        return False
        