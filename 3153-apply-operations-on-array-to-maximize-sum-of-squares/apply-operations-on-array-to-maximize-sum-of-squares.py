from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        # Since nums[i] <= 10^9, 30 bits are enough, but 32 covers standard integers.
        bit_counts = [0] * 32
        
        # Step 1: Count the occurrences of each bit across all numbers
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        ans = 0
        
        # Step 2: Greedily construct the k largest numbers
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            # Step 3: Add the square of the constructed number to total
            ans = (ans + current_num * current_num) % MOD
            
        return ans
