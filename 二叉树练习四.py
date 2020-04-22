class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def get_k_node(self, root, k):
        array_list = self.mid_travel(root)
        print(array_list)
        if k <= 0 or k > len(array_list):
            return
        return array_list[k - 1]

    def mid_travel(self, root):
        if not root:
            return

        self.mid_travel(root.left)
        self.result.append(root.value)
        self.mid_travel(root.right)
        return self.result

    if __name__ == '__main__':
        pass
