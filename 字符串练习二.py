class String:
    def fz(self, str1):
        list01 = str1.split(' ')
        list01.reverse()
        return ' '.join(list01)
        # return ' '.join(list01[::-1])


if __name__ == '__main__':
    s = String()
    l = 'leijin is name my'
    print(s.fz(l))
