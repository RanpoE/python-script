# Duplicate num exists
def has_duplicate(nums: list) -> bool:
    if len(set(nums)) == len(nums):
        return False

    return True


# Missing number
def missing_num(nums: list):
    for _ in range(1, len(nums)+1):
        if _ not in nums:
            return _

    # nums.sort()

    # for i, v in enumerate(nums):
    #     if i != v:
    #         return v - 1

    #     if v == len(nums) - 1:
    #         return v + 1


# Find all missing number
def missing_all_num(nums: list):
    temp = []
    for _ in range(1, len(nums)+1):
        if _ not in nums:
            temp.append(_)

    return temp


# Two sum
def two_sum(nums: list, target: int):
    h_map = {}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in h_map.keys():
            return [h_map[diff], i]
        h_map[v] = i


input1 = [4, 2, 1]
input2 = [9, 6, 4, 2, 3, 5, 7, 0, 1, 1]
input3 = [0, 1, 3]


# How many nums are smaller than
def smaller_nums(nums: list):
    temp = sorted((nums))
    h_map = {}
    for i, v in enumerate(temp):
        if v not in h_map.keys():
            h_map[v] = i
    ret = []
    for v in nums:
        ret.append(h_map[v])

    return ret


print(smaller_nums(input2))
