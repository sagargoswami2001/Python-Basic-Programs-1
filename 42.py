# Write a Python Program to Count the Number 4 in a Given List.
def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count

print(list_count_4([1,4,6,7,4]))
print(list_count_4([1,2,3,4,5,4,6,4]))