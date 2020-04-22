class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def print_tree(self, root):
        if not root:
            return []
        # 不为空的情况
        cur_queue = [root]
        next_queue = []
        while cur_queue:
            node = cur_queue.pop(0)
            print(node.value, end=" ")
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            # 当cur_queue为空时，代表此层打印完毕，交换变量
            if not cur_queue:
                cur_queue, next_queue = next_queue, cur_queue
                print()
