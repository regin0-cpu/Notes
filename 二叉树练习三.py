"""
之字型打印
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def print_tree(selfm, root):
        if not root:
            return []
        level = 1
        cur_stack = [root]
        next_stack = []
        while cur_stack:
            node = cur_stack.pop()
            print(node.value, end=" ")
            if level % 2:
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            else:
                if node.right:
                    next_stack.append(node.right)
                if node.left:
                    next_stack.append(node.left)

                if not cur_stack:
                    cur_stack, next_stack = next_stack, cur_stack
                    level += 1
                    print()

        if __name__ == '__main__':
            pass
