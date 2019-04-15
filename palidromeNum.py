class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse=str(x)[::-1]
        print (reverse)
        
        return(str(x)==reverse)
        