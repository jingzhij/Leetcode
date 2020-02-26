class Solution:
    def reverseWords(self, s: str) -> str:
        res=[i[::-1] for i in s.split(" ")]
        return " ".join(res)
