class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ""
        cur_sym_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '**dummy**', '**dummy**']
        
        while num:
            digit = num % 10
            num = int(num/10)
            if digit % 5 == 4:
                output = cur_sym_list[0] + cur_sym_list[int(digit/5) + 1] + output
            else:
                output = cur_sym_list[1] * int(digit / 5) + (cur_sym_list[0] * (digit % 5)) + output

            cur_sym_list = cur_sym_list[2:]
            
        return output

if __name__ == "__main__":
  s = Solution()
  print s.intToRoman(1947)
