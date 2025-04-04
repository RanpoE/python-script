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
    # Unrestricted
    combo = []
    for i, n in enumerate(nums):
        l, r = 0, len(nums) - 1
        while l < r:
            int_sum = nums[l] + nums[r] + n
            if int_sum == target and l != i and r != i:
                combo.append([nums[l], nums[r], n])
            if int_sum < target:
                l += 1
            else:
                r -= 1

    return combo


def threeSum(nums):
    # Restricted
    triplets = []
    nums.sort()
    for idx, val in enumerate(nums):
        if (idx > 0 and val == nums[idx - 1]):
            continue

        l, r = idx + 1, len(nums) - 1

        while l < r:
            cur_sum = val + nums[l] + nums[r]

            if cur_sum > 0:
                r -= 1
            elif cur_sum < 0:
                l += 1

            else:
                triplets.append([val, nums[l], nums[r]])
                l += 1

                # Keep re-evaluating the remaining
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return triplets


test2 = [1, 2, 3, 4]
mock = [-1, 0, 1, 2, -1, -4]

print(three_sum(test2, 8))
print(threeSum(mock))


def num_is(grid):
    if not grid:
        return

    def bfs(r, c):
        qu = deque()
        qu.append((r, c))

        while qu:
            gr, gc = qu.popleft()

            gdir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for xdir, ydir in gdir:
                sr, sc = gr + xdir, gc + ydir
                if (sr in range(rows) and sc in range(cols) and grid[sr][sc] == '1' and (sr, sc) not in visited):
                    qu.append((sr, sc))
                    visited.add((sr, sc))

    island = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                bfs(row, col)
                island += 1

    return island


print(num_is(grid))


def valid_pairs(nums: list):
    # Check if all item in the list has a pair
    nums.sort()
    print(len(nums))
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i+1]:
            # continue
            return False
    return True


m1 = [1, 1, 2, 2, 3, 3, 4, 4]

print(valid_pairs(m1))


def b_sort(nums: list):
    for i in range(len(nums) - 1):
        for ii in range(i+1, len(nums) - 1):
            if nums[i] > nums[ii]:
                nums[i], nums[ii] = nums[ii], nums[i]

    return nums


uns = [3, 1, 2, 5]

print(b_sort(nums=uns))


def longest_mountain(nums: list):
    ret = 0
    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] > nums[i+1]:
            l = r = i

            while l >= 0 and nums[l] > nums[l-1]:
                l -= 1

            while r < len(nums) and nums[r] > nums[r+1]:
                r += 1   
            ret = max(ret, r-1 + 1)

    return ret


test_mt = [2, 1, 4, 7, 3, 2, 5]
test_m2 = [2, 2, 2]

print(longest_mountain(test_mt))


def contains_dup(nums: list, k: int):
    # Will use sliding window approach

    # - Arrays/Linked list/Linear data/
    # - Finding max/min substring

    # Two pointer was useful for sorted array
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[i-k])

    print(seen)
    return False


test_dup = [1, 2, 3, 1]

print(contains_dup(test_dup, 3))


def minimum_diff(arr: list):
    arr.sort()

    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    res = []

    print(min_diff, " min")
    for i in range(1, len(arr)):
        if (arr[i] - arr[i-1] == min_diff):
            res.append([arr[1-i], arr[i]])

    return res


test_min = [4, 2, 3, 5]

print(minimum_diff(test_min))
