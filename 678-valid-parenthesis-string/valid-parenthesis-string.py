class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = 0  # Minimum possible open parentheses
        cmax = 0  # Maximum possible open parentheses
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:  # char == '*'
                cmin -= 1  # If treated as ')'
                cmax += 1  # If treated as '('
            
            # If maximum possible open parentheses drops below 0,
            # it means there are too many ')' to ever balance out.
            if cmax < 0:
                return False
            
            # cmin cannot drop below 0. If it does, we assume some '*'
            # were treated as empty strings instead of ')'.
            if cmin < 0:
                cmin = 0
                
        # The string is valid only if we can achieve exactly 0 unmatched '('
        return cmin == 0
