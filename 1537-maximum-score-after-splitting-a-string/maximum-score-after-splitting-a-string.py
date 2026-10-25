class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        prefix_zeros = [0] * (n + 1)
        prefix_ones = [0] * (n + 1)
        
        for i in range(n):
            prefix_zeros[i + 1] = prefix_zeros[i] + (1 if s[i] == '0' else 0)
            prefix_ones[i + 1] = prefix_ones[i] + (1 if s[i] == '1' else 0)
            
        total_ones = prefix_ones[n]
        max_score = 0
        
        for i in range(1, n):
            zeros_in_left = prefix_zeros[i]
            ones_in_right = total_ones - prefix_ones[i]
            
            score = zeros_in_left + ones_in_right
            if score > max_score:
                max_score = score
                
        return max_score