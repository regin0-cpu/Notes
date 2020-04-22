"""
二叉树的遍历
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def common_traverse(self, head):
        # 广度遍历：一层一层的遍历
        # 空树：
        if not head:
            return
            # 非空树：
        node_list = [head]
        while node_list:
            node = node_list.pop(0)
            print(node.value, end=" ")
            if node.left:
                node_list.append(node.left)
            if node.eight:
                node_list.append(node.right)

    def front_traverse(self, head):
        # 前序遍历： 根、左、右
        if not head:
            return
        print(head.value, end=" ")
        self.front_traverse(head.left)
        self.front_traverse(head.right)

    def centre_traverse(self, head):
        # 中序遍历：左,根,右
        if not head:
            return
        self.front_traverse(head.left)
        print(head.value, end=" ")
        self.front_traverse(head.right)

    def queen_traverse(self, head):
        # 后序遍历：左,右,根
        if not head:
            return
        self.front_traverse(head.left)
        self.front_traverse(head.right)
        print(head.value, end=" ")


if __name__ == '__main__':
    t = Tree()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t10 = TreeNode(10)
