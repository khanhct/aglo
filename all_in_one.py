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
