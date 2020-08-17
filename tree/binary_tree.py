# encoding=utf-8


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        if L <= root.left.val <= R:
            total = root.val

        def sum_for_lr(node, L, R, total):
            if node.left:
                if L <= node.left.val <= R:
                    total += node.left.val
                return sum_for_lr(node.left, L, R, total)
            if node.right:
                if L <= node.right.val <= R:
                    total += node.right.val
                return sum_for_lr(node.right, L, R, total)

            return total

        return sum_for_lr(root, L, R, total)


def array_to_tree(array):
    root = TreeNode(array[0])
    cur_node = root
    length = len(array)
    for i in range(1, length):
        l, r = 2*i+1, 2*i+2
        if length >= l:
            cur_node.left = TreeNode(array[l])
        if length >= r:
            cur_node.right = TreeNode(array[r])


if __name__ == '__main__':
    pass
