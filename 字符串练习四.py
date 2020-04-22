"""
两个整数之和
"""


class Solution:
    def add(self, n1, n2):
        array_list = [n1, n2]
        return sum(array_list)


if __name__ == '__main__':
    s = Solution()
    r = s.add(1, 3)
    print(r)
