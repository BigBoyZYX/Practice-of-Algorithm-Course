def mode(nums):
    if len(nums) == 1:  # 数组长度为1，返回自身
        return nums[0]
    numDic = {}
    for i in nums:  # 统计每个数字出现的次数，输入到字典numDic
        if i in numDic:
            numDic[i] += 1
            if numDic.get(i) >= (len(nums) + 1) / 2:
                return i
        else:
            numDic[i] = 1
    max(numDic.values())  # 通过max()函数找到字典中的value最大值
    for key, value in numDic.items():  # 再通过value遍历字典找到对应的key
        if value == max(numDic.values()):
            print("众数为：", key, ",", "对应的重数为：", value)


S = [1, 2, 3, 3, 3, 3, 4, 4, 5]
mode(S)
