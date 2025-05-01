import numpy as np

# Test with the following to understand different attributes of the numpy array
# a = [1,2,3]
# a = [[1,2,3]]
a = [[1,2,3],[1,2,3]]
np_a = np.array(a)
def print_array_attr(nd_array):
    print(f"Dimension = {nd_array.ndim}")
    print(f"Shape = {nd_array.shape}")
    print(f"Size = {nd_array.size}")
    print(f"Data Type = {nd_array.dtype}")
    print(f"Item Size = {nd_array.itemsize}")
    print(f"Data = {nd_array.data.obj}")
    print("*"*42)
print_array_attr(np_a)

# linspace
ls_arr = np.linspace(0,1,11)
print_array_attr(ls_arr)

# reshape
rs_arr = np.linspace(1,12, 12).reshape(1,2,6)
print_array_attr(rs_arr)

# indexing
idx_arr = np.arange(12).reshape(4,3)
print_array_attr(idx_arr)
print_array_attr(idx_arr[1,-1])

palette = np.arange(15).reshape(3,5)

# image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
#                   [0, 3, 4, 0]])
image = np.array([(1,2)
                 ,(1,2)])
print_array_attr(palette)
print_array_attr(palette[image, image])

# ix_() function used in matrix operations
a = np.array([2, 3, 4, 5])
