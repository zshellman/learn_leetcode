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
    length = len(array)
    root = TreeNode(array[0])
    for i in range(0, length):
        l, r = 2*i+1, 2*i+2
        print(l, r)
        cur_node = TreeNode(array[i])
        if i == 0:
            root = cur_node
        if length > l:
            cur_node.left = TreeNode(array[l])
        if length > r:
            cur_node.right = TreeNode(array[r])
    return root

def array_to_tree2(array, i):
    length = len(array)
    if i < length:
        root = TreeNode(array[i])
        root.left = array_to_tree2(array, 2 * i + 1)
        root.right = array_to_tree2(array, 2 * i + 2)
        return root
    return None


def test():
    root = array_to_tree2([1, 2, 3, 4, 5, 6], 0)
    def iter_tree(node):
        if not node:
            return
        print(node.val)
        iter_tree(node.left)
        iter_tree(node.right)
    iter_tree(root)


class Tree(object):

    def __init__(self, root):
        self.generate = self.generate_next(root)

    def generate_next(self, root):
        if not root:
            return None
        yield from self.generate_next(root.left)
        if root.val:
            yield root.val
        yield from self.generate_next(root.right)

    def test_next(self):
        for d in self.generate:
            yield d


if __name__ == '__main__':
    root = array_to_tree2([7, 3, 15, None, None, 9, 20], 0)
    a = Tree(root)
    for d in a.generate:
        print(d)
    print(a.test_next())
    print(a.test_next())
