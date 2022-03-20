# Write a Python Program to Check whether a Specified value is contained in a group of Values.

def is_group_member(group_data,n):
    for value in group_data:
        if n == value:
            return True
        return False
print(is_group_member([1,5,8,3], 7))
print(is_group_member([5,8,3], -1))