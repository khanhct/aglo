# SUM
def twoSumI(nums, target):
    result = {}
    for k, v in enumerate(nums):
        sub = target - v
        if sub in result:
            return [result[sub], k]
        result[v] = k


def twoSum(nums, target):
    l, r = 0, len(nums) - 1
    result = []
    while l < r:
        total = nums[l] + nums[r]
        if total > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
            r -= 1
        elif total < target or (l > 0 and nums[l - 1] == nums[l]):
            l += 1
        else:
            result.append([nums[l], nums[r]])
            l += 1
            r -= 1
    return result


def kSum(nums, target, k):
    result = []

    if k == 2:
        return twoSum(nums, target)

    for i in range(len(nums)):
        if i == 0 or nums[i - 1] != nums[i]:
            for sub in kSum(nums[i + 1:], target - nums[i], k - 1):
                result.append([nums[i]] + sub)

    return result


def threeSum(nums, target):
    return kSum(nums, 0, 3)


def fourSum(nums, target):
    return kSum(nums, 0, 4)


def pair(k, arr):
    ret = dict()
    count = 0
    for i, val in enumerate(arr):
        total = val + k
        if total in ret:
            print("{} - {}".format(val, total))
            count += 1
        ret[val] = i
    return count


## String
def is_p(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longest_palindrome(s):
    if not s:
        return
    ret = ''

    for i in range(len(s)):
        old = expand(s, i, i)
        even = expand(s, i, i + 1)
        if len(old) > len(even):
            tmp = old
        else:
            tmp = even
        if len(ret) < len(tmp):
            ret = tmp

    return ret


def expand(s, i, j):
    while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1: j]


def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


def selection_sort(arr):
    s = len(arr)
    for i in range(s):
        lowest_idx = i
        for j in range(i + 1, s):
            if arr[j] < arr[i]:
                lowest_idx = j
        arr[i], arr[lowest_idx] = arr[lowest_idx], arr[i]


def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


def quick_sort(arr, l, r):
    if l < r:
        lo, ro = l, r
        l1 = partition(arr, lo, ro)
        quick_sort(arr, l, l1)
        quick_sort(arr, l1 + 1, r)


def partition(arr, lo, ro):
    l, r = lo, ro
    if l >= r:
        return

    pivot = arr[(l+r)//2]
    while l <= r:
        while arr[l] < pivot and l <= r:
            l += 1

        while arr[r] > pivot and r >= l:
            r -= 1

        if l >= r:
            break

        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return l


## Example
# two sum
# nums, target = [3, 2, 4], 6
# print(twoSum(nums, target))
#
# # three sum
# nums = [-2,0,1,1,2]
# nums.sort()
# print(kSum(nums, 0, 3))

# Palindronearr
# print(longest_palindrome('bacabd'))

# ## PAIR
# arr = [1, 5, 3, 4, 2]
# k = 2
# arr.sort(reverse=True)
# print(pair(2, arr))

## Sort
arr = [22, 5, 1, 18, 99, 0]
# quick_sort(arr, 0, len(arr) - 1)
selection_sort(arr)
print(arr)
# print(insertion_sort(arr))



def bubble_soft(arr):
    s = len(arr)
    for i in range(s):
        for j in range(i + 1, s):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr):
    s = len(arr)
    for i in range(s):
        min_idx = i
        for j in range(i + 1, s):
            if arr[j] < arr[i]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    s = len(arr)
    for i in range(1, s):
        insert_num = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insert_num:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert_num


def quick_sort(arr, l, r):
    if l >= r:
        return

    def partition(lo, ro):
        pivot = arr[(lo + ro)//2]

        while lo <= ro:
            while arr[lo] < pivot and lo <= ro:
                lo += 1

            while arr[ro] > pivot and ro >= lo:
                ro -= 1

            if lo <= ro:
                arr[lo], arr[ro] = arr[ro], arr[lo]
                ro -= 1
                lo += 1

        return lo - 1

    mid = partition(l, r)
    quick_sort(arr, l, mid)
    quick_sort(arr, mid + 1, r)

#
# arr = [1, 3, 3, 2, 5, 0]
# quick_sort(arr, 0, len(arr) - 1)
#
# print(arr)


def isolated_area(arr):
    total = 0
    for i in range(len(arr)):
        for j in  range(len(arr[0])):
            if arr[i][j] == 1:
                dfs(arr, (i, j))
                total += 1

    return total


def dfs(arr, p):
    stack = [p]

    while not stack:
        i, j = stack.pop()
        arr[i][j] = 2

        if arr[i - 1] == 0:
            stack.insert(0, (i, j))


def int_para(val):
    num_arr = []
    while val > 0:
        mod = val%10
        num_arr.insert(0, mod)
        val = val//10

    def is_p():
        l, r = 0, len(num_arr) - 1
        while l <= r:
            if num_arr[l] != num_arr[r]:
                return False
            l += 1
            r -= 1
        return True

    return is_p()

# def expand(arr, i, j):
#     while arr[i] == arr[j]:

# print(int_para(124521))

# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]


def word_search(board, word):
    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(board, visited, (i, j), word, 1):
                    return True
    return False


def dfs(board, visited, p, word, idx):
    s1 = len(board) - 1
    s2 = len(board[0]) - 1
    i, j = p
    # visited.add((i, j))
    if idx >= len(word):
        return True

    if i + 1 <= s1 and (i+1, j) not in visited and board[i+1][j] == word[idx]:
        if dfs(board, visited, (i+1, j), word, idx + 1):
            return True

    if i - 1 >= 0 and (i-1, j) not in visited and board[i-1][j] == word[idx]:
        if dfs(board, visited, (i-1, j), word, idx + 1):
            return True

    if j + 1 <= s2 and (i, j + 1) not in visited and board[i][j + 1] == word[idx]:
        if dfs(board, visited, (i, j + 1), word, idx + 1):
            return True

    if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == word[idx]:
        if dfs(board, visited, (i, j - 1), word, idx + 1):
            return True


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, visited, (i, j), word, 1):
                        return True
        return False

    def dfs(self, board, visited, p, word, idx):
        s1 = len(board) - 1
        s2 = len(board[0]) - 1
        i, j = p
        # visited.add((i, j))
        tmp = board[i][j]
        board[i][j] = '#'
        if idx >= len(word):
            return True

        if i + 1 <= s1 and (i + 1, j) not in visited and board[i + 1][j] == word[idx]:
            if self.dfs(board, visited, (i + 1, j), word, idx + 1):
                return True

        if i - 1 >= 0 and (i - 1, j) not in visited and board[i - 1][j] == word[idx]:
            if self.dfs(board, visited, (i - 1, j), word, idx + 1):
                return True

        if j + 1 <= s2 and (i, j + 1) not in visited and board[i][j + 1] == word[idx]:
            if self.dfs(board, visited, (i, j + 1), word, idx + 1):
                return True

        if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == word[idx]:
            if self.dfs(board, visited, (i, j - 1), word, idx + 1):
                return True
        board[i][j] = tmp

# board = [["C","A","A"],
#          ["A","A","A"],
#          ["B","C","D"]]

board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"
# sol = Solution()
# print(sol.exist(board, word))


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and (i, j) not in visited:
                    visited.add((i, j))
                    self.draw(matrix, visited, i, j)

    def draw(self, matrix, visited, i, j):
        s1 = len(matrix) - 1
        s2 = len(matrix[0]) - 1
        while s1 >= 0:
            if matrix[s1][j] != 0:
                visited.add((s1, j))
            matrix[s1][j] = 0
            s1 -= 1

        while s2 >= 0:
            if matrix[i][s2] != 0:
                visited.add((i, s2))
            matrix[i][s2] = 0
            s2 -= 1


# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#
# sol = Solution()
# print(sol.setZeroes(matrix))
# print(matrix)


class Solution:
    def num_decodings(self, s) -> int:
        total = 0
        self.ds(s, total)
        return total

    def ds(self, s, total):
        sz = len(s)
        i = 0
        while i < sz:
            if int(s[i]) <= 2:
                total += 1
                if i + 1 >= sz:
                    break
                self.ds(s[i + 1:], total)
                if i + 1 < sz and int(s[i + 1]) <= 6:
                    total += 1
                    if i + 2 >= sz:
                        break
                    self.ds(s[i + 2:], total)
            else:
                total += 1
                if i + 1 >= sz:
                    break
                self.ds(s[i + 1:], total)



s = "226"
sol = Solution()
print(sol.num_decodings(s))
