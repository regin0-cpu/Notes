class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def convert_tree_link(self, root):
        array_list = self.mid_travle(root)

        if not len(array_list):
            return None
        if len(array_list) == 1:
            return

        array_list[0].left = None
        array_list[0].right = array_list[1]
        array_list[-1].left = array_list[-2]
        array_list[-1].right = None

        for i in range(1, len(array_list) - 1):
            array_list[i].left = array_list[i - 1]
            array_list[i].right = array_list[i + 1]
        return array_list[0]

    def mid_travle(self, root):
        if not root:
            return
        self.mid_travle(root.left)
        self.result.append(root)
        self.mid_travle(root.right)
        return self.result


if __name__ == '__main__':
    pass
