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


def min_time_to_visit_points(points: list):
    res = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        res += max(abs(y2 - y1), abs(x2-x1))
        x1, y1 = x1, y2
    return res


points = [[1, 1], [3, 4], [-1, 0]]

print(min_time_to_visit_points(points))


def spiral_order(matrix):
    ret = []

    while matrix:
        # get the first array on matrix
        ret += (matrix.pop(0))
        print(matrix)
        # Iterate the row and get each last element
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())

        # Reverse the row/list and add
        if matrix:
            ret += (matrix.pop()[::-1])

        # append all first el of all row/list
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))

    return ret


test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(spiral_order(test))
