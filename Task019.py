#  Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,
# K – положительное число.
# [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3] (сдвиг на 2 элемента)

nums = [1, 2, 3, 4, 5, 6, 7]

sdvig = int(input()) % len(nums)

# for _ in range(sdvig):
#     nums.insert(0, nums.pop(len(nums)-1))
# print(nums)

nums = nums[-sdvig::] + nums[:-sdvig:]
print(nums)
