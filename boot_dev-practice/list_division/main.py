def divide_list(nums, divisor):
    divided_list = []
    for num in nums:
        divided_list.append(num / divisor)

    return divided_list

num_list = [13, 14, 99, 94, 42]
divided_list = divide_list(num_list, 2)
print(divided_list)