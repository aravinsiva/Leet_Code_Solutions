class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0        
        i = 0
        if not str[i].isdigit() and str[i] not in ('-', '+'):
            return 0
        if str[i] in ('-', '+'):
            i += 1 
        digits = []
        while(i < len(str) and str[i].isdigit()):
            digits.append(str[i])
            i += 1
        integer = 0
        while len(digits) > 0:
            integer += 10 ** (len(digits) - 1) * int(digits.pop(0))
        if str[0] == '-':
            integer *= -1
        if integer < (-2) ** 31:
            return (-2) ** 31
        elif integer >= 2 ** 31:
            return 2 ** 31 - 1
        else:
            return integer 
        
        