class String:
    def yd(self, str1, k):
        left_s = str1[:k]
        right_s = str1[k:]
        return right_s + left_s


if __name__ == '__main__':
    s = String()
    str2 = "abcde"
    print(s.yd(str2, 2))
