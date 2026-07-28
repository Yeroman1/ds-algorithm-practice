class Solution:
    def combine(self, n: int, k: int):
        result = []

        def backtrack(start, current):
            # Base case: combination size reached
            if len(current) == k:
                result.append(current.copy())
                return

            # Try every possible number
            for i in range(start, n + 1):
                current.append(i)

                # Move to next number
                backtrack(i + 1, current)

                # Remove last number (backtrack)
                current.pop()

        backtrack(1, [])

        return result