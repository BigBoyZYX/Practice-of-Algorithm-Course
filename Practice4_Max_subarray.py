# A是一个包含负数的列表,合并算法是要返回一个跨越分割点mid的最大数组
def find_max_crossing_subarray(A, low, mid, high):
    sumleft = float("-inf")
    s = 0
    for i in range(mid, -1, -1):
        s += A[i]
        if s > sumleft:
            sumleft = s
            maxleft = i
    sumright = float("-inf")
    s = 0
    for j in range(mid + 1, high + 1):
        s += A[j]
        if s > sumright:
            sumright = s
            maxright = j
    return maxleft, maxright, sumleft + sumright


# low代表列表A的最小下标，high代表最大下标，函数返回A所包含的最大连续数组
def find_max_subarray(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        (leftlow, lefthigh, leftsum) = find_max_subarray(A, low, mid)
        (rightlow, righthigh, rightsum) = find_max_subarray(A, mid + 1, high)
        (crosslow, crosshigh, crosssum) = find_max_crossing_subarray(A, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif rightsum >= leftsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(A)
low, high, sum = find_max_subarray(A, 0, len(A) - 1)
print("起始位置(从1开始数):", low+1, "终止位置:", high+1, "最大子数组的和为:", sum)
print("最大子数组为:", A[low:high + 1])
