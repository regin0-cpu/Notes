class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def fuse(self, head1, head2):
        if head1 and head2:
            if head1.value < head2.value:
                top = head1
                head1 = head1.next
            else:
                top = head2
                head2 = head2.next
            p = top
        elif head1:
            return head1
        else:
            return head2
        while head1 and head2:
            if head1.value <= head2.value:
                top.next = head1
                head1 = head1.next
            else:
                top.next = head2
                head2 = head2.next
            top = top.next
        if not head1:
            top.next = head2
        elif not head2:
            top.next = head1
        return p

    def tar(self, link):
        head = link
        while head:
            print(head.value)
            head = head.next


if __name__ == '__main__':
    s = Solution()
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(4)
    p4 = Node(7)
    p5 = Node(8)
    p6 = Node(9)

    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6

    p7 = Node(3)
    p8 = Node(5)
    p9 = Node(6)
    p7.next = p8
    p8.next = p9
    p10 = s.fuse(p1, p7)
    s.tar(p10)
