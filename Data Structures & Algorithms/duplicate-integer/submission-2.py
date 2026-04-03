class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #what data structure we do like for dups?
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False