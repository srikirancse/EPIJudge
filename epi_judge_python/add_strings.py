class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_ptr = len(num1) - 1
        num2_ptr = len(num2) - 1
        result = ''
        carry = 0

        while num1_ptr >= 0 or num2_ptr >= 0:
          if num1_ptr >= 0 and num2_ptr >= 0: 
            sum = int(num1[num1_ptr]) + int(num2[num2_ptr]) + carry
            num1_ptr, num2_ptr = num1_ptr - 1, num2_ptr - 1
          elif num1_ptr >= 0: 
            sum = int(num1[num1_ptr]) + carry
            num1_ptr -= 1
          else: 
            sum = int(num2[num2_ptr]) + carry
            num2_ptr -= 1
          carry = sum // 10
          sum = int(sum % 10)
          result = str(sum) + result

        
        if carry == 1:
          result = '1' + result

        return result

solution = Solution()
print(solution.addStrings('9', '9'))