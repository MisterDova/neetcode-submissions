class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(word)):
            left = word[i]
            right = word[-i-1]
            if left != right:
                return False
        return True