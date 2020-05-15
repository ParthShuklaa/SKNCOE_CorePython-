"""


import numpy as np


list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6, 5]

arr1 = np.array(list1)
arr2 = np.array(list2)


# Multiplying both lists directly would give an error.
print(arr1*arr2)
"""



# Python program for basic slicing.
import numpy as np

# Arrange elements from 0 to 19
a = np.arange(20)
print("\n Array is:\n ", a)

# a[start:stop:step]
print("\n a[-8:17:1]  = ", a[-8:17:1])

# The : operator means all elements till the end.
print("\n a[10:]  = ", a[10:])