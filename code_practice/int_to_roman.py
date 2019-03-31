class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ""
        cur_sym_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        
        while num:
            digit = num % 10
            num = int(num/10)
            if digit == 0:
                pass
            elif digit < 4:
                output = (cur_sym_list[0] * digit) + output
            elif digit == 4:
                output = cur_sym_list[0] + cur_sym_list[1] + output
            elif digit < 9:
                output = cur_sym_list[1] + (cur_sym_list[0] * (digit - 5)) + output
            else:
                output = cur_sym_list[0] + cur_sym_list[2] + output
                
            cur_sym_list = cur_sym_list[2:]
            
        return output

if __name__ == "__main__":
  s = Solution()
  print s.intToRoman(1947)
