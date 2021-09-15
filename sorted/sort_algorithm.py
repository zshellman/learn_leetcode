# encoding=utf-8
import random


def swap():
    pass


def bubble_sort(sort_list):
    """
    冒泡排序
    :return:
    """
    for i in range(0, len(sort_list)):
        for j in range(0, len(sort_list) - 1 - i):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


def select_sort(sort_list):
    """
    选择排序:
    找到最小值，把最小值放到第一个
    重复上一步
    :param sort_list:
    :return:
    """
    for i in range(0, len(sort_list)):
        min_value = sort_list[i]
        min_index = i
        for j in range(i + 1, len(sort_list)):
            if min_value > sort_list[j]:
                min_index, min_value = j, sort_list[j]
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
    return sort_list


def inset_sort(sort_list):
    """
    插入排序

    :param sort_list:
    :return:
    """
    for i in range(0, len(sort_list)):
        pre_index = i - 1
        cur = sort_list[i]
        # 前一个大于当前值，则把前一个往后挪一位
        while pre_index >= 0 and sort_list[pre_index] > cur:
            sort_list[pre_index + 1] = sort_list[pre_index]
            pre_index -= 1
        sort_list[pre_index + 1] = cur
    return sort_list


def merge_sort(sort_list):
    """
    归并排序
    :param sort_list:
    :return:
    """
    if len(sort_list) < 2:
        return sort_list
    left = sort_list[0: len(sort_list) // 2]
    right = sort_list[len(sort_list) // 2:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    # 对2个有序数组进行一个一个的对比，插入新的数组
    ret = []
    while left and right:
        if left[0] <= right[0]:
            ret.append(left.pop(0))
        else:
            ret.append(right.pop(0))
    # 此时要么剩left要么剩right，但是left和right本身就是有序的，直接加入进来即可
    if left:
        ret += left
    if right:
        ret += right
    return ret


if __name__ == '__main__':
    a = [random.randint(0, 10) for i in range(0, 10)]
    print(a)
    print(merge_sort(a))
