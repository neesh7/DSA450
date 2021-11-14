# Finding Minimum element of an array

arr = [10, 23, 44, 5, 3, 54]

# Approach 1: Take Minimum Variable as 0 and keep on updating it

# Logic to Find Minimum
Min = arr[0]
for i in arr:  # Time Complexity for this algo = o(n)
    if Min > i:
        Min = i
print("Minimum Value in the array is {}".format(Min))

# Logic to Find Maximum
Max = arr[0]
for j in arr:  # Time Complexity for this algo = o(n)
    if Max < i:
        Max = i

print("Maximum Value in the array is {}".format(Max))
