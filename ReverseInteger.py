# -*- coding:utf-8 -*-

'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''

'''
    1.首先，-10到10之间的整数原样输出
    2.将输入的值取绝对值，删除正负号
    3.将绝对值转换为字符串
    4.对字符串遍历反向存进一个空字符串
    5.把反向字符串转为整数，判断原输入值是否为负数
    6.判断是否溢出
    7.输出
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x

        y = abs(x)
        s = ''
        y = str(y)
        for i in range(len(y)):
            s += y[len(y) - i - 1]

        y = int(s)
        if x < 0:
            y = -y

        if -2147483648 < y < 2147483647:
            return y
        else:
            return 0


a = Solution()
print a.reverse(-12323)