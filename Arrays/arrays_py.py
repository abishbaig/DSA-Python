import array as arr

array: arr.array = arr.array("i",[1,2,3])

# Appending = T.C = O(1) {Amortized}
array.append(4)

# Deletion = T.C = O(n)
print(array.pop(2))


# Traversing = T.C = O(n)
for i in array:
    print(i) 