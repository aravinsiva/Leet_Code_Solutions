class Solution(object):
    def reverse(self, number):
        """
        :type x: int
        :rtype: int
        """
        reverse=0
         
        if (number>0):
            while (number > 0):
                lastDigit = number % 10
                reverse = (reverse * 10) + lastDigit
                number = number / 10
                
            if (reverse<2**-31 or reverse>2**31-1):
                return 0
                
            return(reverse)

        else:
            number=number*-1
            while (number > 0):
                lastDigit = number % 10
                reverse = (reverse * 10) + lastDigit
                number = number / 10
                
                
            if (reverse<2**-31 or reverse>2**31-1):
                return 0
                
            return(reverse*-1)