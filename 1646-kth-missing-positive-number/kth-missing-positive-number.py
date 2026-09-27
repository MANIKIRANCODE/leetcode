class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing_count = 0
        current = 1
        while(missing_count != k):
            if current in arr:
                current += 1
            else:
                missing_count += 1
                current += 1
            if missing_count == k:
                return current-1
