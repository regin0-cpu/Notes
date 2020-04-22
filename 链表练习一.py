class Link:
    # 节点类
    def __init__(self, data):
        self.data = data
        self.next = None

    def con(self, list1):
        # 连接节点
        pass


class LinkDispose:
    # 处理类
    # 删除重复节点：
    def dispose(self, link):
        head = link
        while head.next:
            l = head.next
            if l.data == head.data:
                head.next = l.next
            else:
                head = head.next
        return link

    # 遍历链表：
    def tra(self, link):
        head = link
        while head:
            print(head.data)
            head = head.next


if __name__ == '__main__':
    l = Link(10)
    l1 = Link(20)
    l2 = Link(20)
    l3 = Link(20)
    l4 = Link(30)
    l.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    lt = LinkDispose()
    k = lt.dispose(l)
    lt.tra(k)
