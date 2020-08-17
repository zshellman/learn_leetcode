# encoding=utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_node = ListNode(head.val)
        ori_cur_node = head
        while ori_cur_node.next:
            new_head = ListNode(ori_cur_node.next.val)
            new_head.next = head_node
            head_node = new_head
            ori_cur_node = ori_cur_node.next
        return head_node

    def reverse_list(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return cur


    def swapPairs(self, head):
        cur_node = head
        if head.next:
            # get third node
            third = head.next.next
            if third:
                third = self.swapPairs(third)
            # second node reference first node
            cur_node = head.next
            cur_node.next = head
            # first node reference third node
            head.next = third
        return cur_node

    def swapPairs2(self, head):
        if not head or not head.next:
            return head
        first_node, second_node = head, head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        has_pass_index = []
        cur_node = id(head)
        while head.next:
            if cur_node in has_pass_index:
                return True
            else:
                has_pass_index.append(cur_node)
                cur_node = id(head.next)
                head = head.next
        return False

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        has_pass_index = []
        while head.next:
            if head in has_pass_index:
                return has_pass_index[has_pass_index.index(head)]
            else:
                has_pass_index.append(head)
                head = head.next
        return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        right_str = {"(": ")", "[": "]", "{": "}"}
        for i in range(0, len(s)):
            if s[i] in right_str.keys():
                stack.append(s[i])
            elif len(stack) > 0 and right_str.get(stack.pop()) == s[i]:
                pass
            else:
                return False

        return len(stack) == 0



def init_list(n):
    head = ListNode(1)
    cur_node = head
    for i in range(2, n+1):
        next_node = ListNode(i)
        cur_node.next = next_node
        cur_node = next_node

    return head


def print_link_list(head):
    while head:
        print(head.val)
        head = head.next
