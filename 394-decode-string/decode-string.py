class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i):
            res = ""
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])

                elif s[i] == '[':
                    inner, i = helper(i + 1)
                    res += inner * num
                    num = 0

                elif s[i] == ']':
                    return res, i

                else:
                    res += s[i]

                i += 1

            return res, i

        return helper(0)[0]