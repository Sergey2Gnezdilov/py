"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
https://leetcode.com/problems/roman-to-integer/
Symbol       Value
I             1
V             5
X             10
L             50
C             100 
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
RomanDic = {}
RomanDic[1] = 'I'
RomanDic[2] = 'II'
RomanDic[3] = 'III'
RomanDic[4] = 'IV'
RomanDic[5] = 'V'
RomanDic[6] = 'VI'
RomanDic[7] = 'VII'
RomanDic[8] = 'VIII'
RomanDic[9] = 'IX'
RomanDic[10] = 'X'
RomanDic[20] = 'XX'
RomanDic[30] = 'XXX'
RomanDic[40] = 'XL'
RomanDic[50] = 'L'
RomanDic[60] = 'LX'
RomanDic[70] = 'LXX'
RomanDic[80] = 'LXXX'
RomanDic[90] = 'XC'
RomanDic[100] = 'C'
RomanDic[200] = 'CC'
RomanDic[300] = 'CCC'
RomanDic[400] = 'CD'
RomanDic[500] = 'D'
RomanDic[600] = 'DC'
RomanDic[700] = 'DCC'
RomanDic[800] = 'DCCC'
RomanDic[900] = 'CM'
RomanDic[1000] = 'M'
RomanDic[2000] = 'MM'
RomanDic[3000] = 'MMM'
output=0
s = "MCMX"
# sorted(RomanDic.keys(),reverse=True):
roman_dic= {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
position,output=0,0
while position < len(s):
    if (position < len(s) - 1 and s[position] + s[position + 1] in roman_dic):
                output += roman_dic[s[position] + s[position + 1]]
                print (roman_dic[s[position] + s[position + 1]], position)
                position += 2
    else:
        output += roman_dic[s[position]]
        print (position, roman_dic[s[position]])
        position += 1
            
print (output)
