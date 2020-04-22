class Solution:
    def string_r(self, str1):
        return str1.replace(' ', '%20')


if __name__ == '__main__':
    s = Solution()
    string = "we Are Family"
    re = s.string_r(string)
    print(re)
