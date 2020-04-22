class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_first(self, head1, head2):
        stack1 = []
        stack2 = []
        while head1:
            stack1.append(head1)
            head1 = head1.next
        while head2:
            stack2.append(head2)
            head2 = head2.next

        node = None
        while stack2 and stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 is node2:
                node = node2
                continue
            else:
                break
        return node


if __name__ == '__main__':
    s = Solution()
    p1 = Node(100)
    p2 = Node(200)
    p3 = Node(300)
    p4 = Node(400)
    p5 = Node(666)
    p6 = Node(888)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p5.next = p6
    p6.next = p3
    s2 = Solution()
    f = s2.get_first(p1, p5)
    print(f.value)
