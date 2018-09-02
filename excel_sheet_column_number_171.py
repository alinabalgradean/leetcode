'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
# Beats 90% of the running times

import string

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = list(string.ascii_uppercase)
        alphabeto = {j:i for i,j in enumerate(alphabet)}
        if len(s) == 1:
            num = alphabeto[s] + 1 
        else:
            num = 0 
            for lt in s:
                num = num * 26 + alphabeto[lt] + 1 
        return num
