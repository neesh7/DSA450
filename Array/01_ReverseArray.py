# This code is problem 1 for Reversing an String

arr = [1, 2, 3]

# Using Slice to revere the List
# Approach 1: Use of Negative indexing to reverse the array
print(arr[::-1])

# Approach 2: Iterative method --> using multiple swapping to perform the reverse
len_arr = len(arr)
print(len_arr)
z = 1
for i in range(len_arr - z):  # Complexity = o(3) --> len(arr)
    if i < len_arr - z:
        arr[i], arr[len_arr - 1] = arr[len_arr - 1], arr[i]
    elif i == len_arr - z:
        pass
    z += 1

print(arr)
