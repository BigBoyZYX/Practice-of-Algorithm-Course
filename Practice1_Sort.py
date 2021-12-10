from random import randint
import copy

l1 = [randint(1, 10000) for i in range(1000)]
l2 = copy.copy(l1)
l3 = copy.copy(l1)
l4 = copy.copy(l1)
l5 = copy.copy(l1)
print("随机生成1000个数：", l1)


# 冒泡排序
def bubble_sort(L):
    for i in range(len(L) - 1):  # 遍历数组
        x = i
        y = L[i]
        j = i + 1
        while j < len(L):  # 从左向右，相邻两个数比较
            if y > L[j]:  # 如果前面的数比后面的大，就交换他们两个
                x = j
                y = L[j]
            j += 1
        z = L[i]
        L[i] = L[x]
        L[x] = z
    return L


print("冒泡排序结果：", bubble_sort(l1))


# 插入排序
def insert_sort(L):
    for j in range(1, len(L)):  # j从头到尾遍历数组
        k = L[j]  # k保存L[j]的值用来向前比较
        i = j - 1  # j从它前面的数开始比较
        while i >= 0 and L[i] > k:  # k与L[i]比较
            L[i + 1] = L[i]  # 如果L[i]比k大，L[i]向后移
            i -= 1
        L[i + 1] = k  # 否则如果L[i]小于或等于k，k插入到L[i]后面
    return L


print("插入排序结果：", insert_sort(l2))


# 合并排序
def merge(left, right):  # 合并过程
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):  # 遍历子数组进行合并
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):  # 合并排序
    if len(L) < 2:  # 仅有一个元素，递归终止
        return L[:]
    else:
        middle = len(L) // 2  # 计算子问题规模
        left = merge_sort(L[:middle])  # 递归求解子问题
        right = merge_sort(L[middle:])
        return merge(left, right)


print("合并排序结果：", merge_sort(l3))


# 快速排序
def quick_sort(L, start, end):
    if start >= end:  # 当没有或只有一个数时，不需要排序
        return L
    left = start
    right = end  # 定义两个游标，分别指向0和末尾位置
    mid = L[left]  # 把0位置的数据作为主元
    while left < right:
        while left < right and L[right] >= mid:  # 从右向左找小于主元的值，放到left游标位置
            right -= 1
        L[left] = L[right]
        while left < right and L[left] < mid:  # 从左向右找大于主元的值，放到right游标位置
            left += 1
        L[right] = L[left]
    L[left] = mid  # 把主元放到中间位置，left=right
    quick_sort(L, start, left - 1)  # 递归处理左边的数据
    quick_sort(L, left + 1, end)  # 递归处理右边的数据
    return L


print("快速排序结果：", quick_sort(l4, 0, len(l4) - 1))


# 降序插入排序
def insert_sort(L):
    for j in range(1, len(L)):  # j从头到尾遍历数组
        k = L[j]  # k保存L[j]的值用来向前比较
        i = j - 1  # j从它前面的数开始比较
        while i >= 0 and L[i] < k:  # k与L[i]比较
            L[i + 1] = L[i]  # 如果L[i]比k小，L[i]向后移
            i -= 1
        L[i + 1] = k  # 否则如果L[i]大于等于k，k插入到L[i]后面
    return L


print("逆序插入排序结果：", insert_sort(l5))
