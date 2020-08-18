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
        def sum_for_lr(node, L, R, total):
            if not node:
                return total
            if L <= node.val <= R:
                total += node.val
            total = sum_for_lr(node.left, L, R, total)
            total = sum_for_lr(node.right, L, R, total)

            return total

        return sum_for_lr(root, L, R, 0)


def array_to_tree(array, index):
    if index < len(array):
        node = TreeNode(array[index])
    else:
        return None

    node.left = array_to_tree(array, 2*index + 1)
    node.right = array_to_tree(array, 2*index + 2)

    return node

def print_binary_tree(root):
    if not root:
        return
    print(root.val)
    print_binary_tree(root.left)
    print_binary_tree(root.right)


if __name__ == '__main__':
    a = [10,5,15,3,7,13,18,1,None,6]

    root = array_to_tree(a, 0)
    print('---------------')
    print_binary_tree(root)
    print('------------')
    s = Solution()
    print(s.rangeSumBST(root, 6, 10))

