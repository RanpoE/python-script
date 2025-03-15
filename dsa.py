from collections import deque

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

print(two_sum(input1, 3))


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


# breadth first search
# BFS -> seaches from children nodes to grandchildren nodes
def number_of_island(grid):
    if not grid:
        return

    def bfs(r, c):
        search_queue = deque()
        search_queue.append((r, c))
        while search_queue:
            row, col = search_queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                r, c = row+dr, col+dc

                if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited):
                    search_queue.append((r, c))
                    visited.add((r, c))

    count = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                bfs(row, col)
                count += 1

    return count
# Time complexity -> O(4 * n* m) = O(n*m)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "0", "0", "0", "0"],
    ["1", "1", "0", "0", "0"]
]

print(number_of_island(grid))


# Two pointer approach
# Time complexity -> O(n)
# Greedy algorithm -> a type of optimization algorithm that makes locally optimal choices at each step
# to find a globally optimal solution. It operates on the principle of "taking the best option now"
# without considering the long-term consequences.

def buy_stock(nums: list):
    l, r = 0, 1
    p = 0
    while r != len(nums):
        if nums[r] > nums[l]:
            prof = nums[r] - nums[l]
            p = max(prof, p)
        else:
            l += 1

        r += 1

    return p


tt = [7, 1, 5, 2, 6]
print(buy_stock(tt))


def sorted_squares(nums: list):
    # sqr = [n ** 2 for n in nums]
    # sqr.sort()
    # Two pointers O(n)
    sqr = deque()
    l, r = 0, len(nums) - 1

    while l <= r:
        if abs(nums[l]) < abs(nums[r]):
            sqr.appendleft((nums[r] ** 2))
            r -= 1
        else:
            sqr.appendleft((nums[l] ** 2))
            l += 1

    return list(sqr)


n = [-4, -1, 0, 3, 10]
print(sorted_squares(n))
# Iteration O(n)
# Sorting (O (n log(n)))


def two_sum_p2(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        int_sum = nums[l] + nums[r]
        if int_sum == target:
            return {l + 1, r + 1}

        if int_sum < target:
            l += 1
        else:
            r -= 1


test1 = [2, 7, 11, 15]

print(two_sum_p2(test1, 9))


def three_sum(nums, target):
    for i, n in enumerate(nums):
        l, r = 0, len(nums) - 1
        while l < r:
            int_sum = nums[l] + nums[r] + n
            if int_sum == target and l != i and r != i:
                return {nums[l], nums[r], n}

            if int_sum < target:
                l += 1
            else:
                r -= 1


test2 = [1, 2, 3, 4]

print(three_sum(test2, 7))
