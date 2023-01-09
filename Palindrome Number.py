class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = x
        remainder = -1
        result = ""
        while number >= 1:
            remainder = int(number % 10)
            number = number / 10
            result = result + str(remainder)

        if result == str(x):
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(121))
