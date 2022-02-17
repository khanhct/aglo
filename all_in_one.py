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


##  String
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


def countInversions(arr):
    pass


def quick_sort(arr, l, r):
    if l < r:
        lo, ro = l, r
        lo, ro = partition(arr, lo, ro)
        quick_sort(arr, l, lo)
        quick_sort(arr, ro, r)


def partition(arr, lo, ro):
    l, r = lo, ro
    if l >= r:
        return

    pivot = arr[r]
    r -= 1
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

    return l, r


def insertion_sort(arr):
    pass


## Example
# two sum
# nums, target = [3, 2, 4], 6
# print(twoSum(nums, target))
#
# # three sum
# nums = [-2,0,1,1,2]
# nums.sort()
# print(kSum(nums, 0, 3))

# Palindrone
# print(longest_palindrome('bacabd'))

# ## PAIR
# arr = [1, 5, 3, 4, 2]
# k = 2
# arr.sort(reverse=True)
# print(pair(2, arr))

## Sort
arr = [2, 4, 1]
print(quick_sort(arr, 0, len(arr) - 1))
# print(insertion_sort(arr))
