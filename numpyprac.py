
import numpy as np

print("=== NumPy Basic and Common Instructions ===\n")

# 1️⃣ Array Creation
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Array a:", a)
print("Array b:\n", b)

# 2️⃣ Array of zeros, ones, and identity
z = np.zeros((2, 3))
o = np.ones((2, 3))
i = np.eye(3)
print("\nZeros:\n", z)
print("Ones:\n", o)
print("Identity:\n", i)

# 3️⃣ Range and Linspace
r = np.arange(0, 10, 2)
l = np.linspace(0, 1, 5)
print("\nArange:", r)
print("Linspace:", l)

# 4️⃣ Random Arrays
rand = np.random.rand(2, 2)
rand_int = np.random.randint(1, 10, (2, 3))
print("\nRandom Float Array:\n", rand)
print("Random Integer Array:\n", rand_int)

# 5️⃣ Basic Info
print("\nShape of b:", b.shape)
print("Size of b:", b.size)
print("Data type of b:", b.dtype)

# 6️⃣ Reshaping and Flattening
reshaped = b.reshape(3, 2)
flattened = b.flatten()
print("\nReshaped b (3x2):\n", reshaped)
print("Flattened b:", flattened)

# 7️⃣ Indexing & Slicing
print("\nFirst row of b:", b[0])
print("Element at (1,2):", b[1, 2])
print("Slice of a[1:3]:", a[1:3])

# 8️⃣ Basic Math Operations
print("\nAddition:", a + 5)
print("Multiplication:", a * 2)
print("Array Addition (a+a):", a + a)
print("Array Multiplication (a*a):", a * a)

# 9️⃣ Matrix Operations
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print("\nMatrix Multiplication:\n", np.dot(x, y))
print("Elementwise Multiplication:\n", x * y)
print("Transpose:\n", x.T)

# 🔟 Useful Math Functions
print("\nSquare root:", np.sqrt(a))
print("Exponent:", np.exp(a))
print("Sine:", np.sin(a))
print("Mean:", np.mean(a))
print("Standard deviation:", np.std(a))
print("Sum:", np.sum(a))
print("Max:", np.max(a))
print("Min:", np.min(a))

# 1️⃣1️⃣ Conditional Operations
cond = a > 2
print("\nCondition (a > 2):", cond)
print("Elements > 2:", a[cond])

# 1️⃣2️⃣ Stacking Arrays
v_stack = np.vstack((a, a))
h_stack = np.hstack((a, a))
print("\nVertical Stack:\n", v_stack)
print("Horizontal Stack:\n", h_stack)

# 1️⃣3️⃣ Copy vs View
c = a.copy()
v = a.view()
a[0] = 100
print("\nOriginal a (modified):", a)
print("Copy c (unchanged):", c)
print("View v (reflects change):", v)


#slicing examples


print("=== NumPy Slicing Examples (1D, 2D, 3D) ===\n")

# 1️⃣ 1D Array Slicing
arr1 = np.array([10, 20, 30, 40, 50, 60])
print("1D Array:", arr1)
print("Slice [1:4]:", arr1[1:4])        # elements at index 1,2,3
print("Slice [:3]:", arr1[:3])          # first 3 elements
print("Slice [::2]:", arr1[::2])        # every 2nd element
print("Slice [-3:]:", arr1[-3:])        # last 3 elements
print()

# 2️⃣ 2D Array Slicing
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print("2D Array:\n", arr2)

# Row and Column access
print("\nFirst row:", arr2[0, :])
print("First column:", arr2[:, 0])
print("Subarray (first 2 rows, first 2 cols):\n", arr2[0:2, 0:2])
print("Middle element:", arr2[1, 1])
print("Last column:", arr2[:, -1])

# Step slicing
print("\nEvery other element in first row:", arr2[0, ::2])
print("Every other row:\n", arr2[::2, :])
print()

# 3️⃣ 3D Array Slicing
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print("3D Array:\n", arr3)
print("Shape:", arr3.shape)  # (2 blocks, 2 rows, 3 cols)

print("\nFirst block (index 0):\n", arr3[0])
print("Second block (index 1):\n", arr3[1])
print("First row of first block:", arr3[0, 0])
print("Element at [1, 1, 2]:", arr3[1, 1, 2])
print("All blocks, first row only:\n", arr3[:, 0, :])
print("All blocks, last column only:\n", arr3[:, :, -1])
print()

# 4️⃣ Slicing with View vs Copy
sub_slice = arr2[0:2, 0:2]  # this creates a view, not a copy
print("Before modification:\n", arr2)
sub_slice[0, 0] = 999
print("\nAfter modifying sub-slice:")
print("Modified sub-slice:\n", sub_slice)
print("Original array also changed (view behavior):\n", arr2)

'''  output 
Array a: [1 2 3 4]
Array b:
 [[1 2 3]
 [4 5 6]]

Zeros:
 [[0. 0. 0.]      
 [0. 0. 0.]]      
Ones:
 [[1. 1. 1.]
 [1. 1. 1.]]
Identity:
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Arange: [0 2 4 6 8]
Linspace: [0.   0.25 0.5  0.75 1.  ]

Random Float Array:
 [[0.69330951 0.33486144]
 [0.85122669 0.82188783]]
Random Integer Array:
 [[2 5 7]
 [8 6 1]]

Shape of b: (2, 3)
Size of b: 6
Data type of b: int64

Reshaped b (3x2):
 [[1 2]
 [3 4]
 [5 6]]
Flattened b: [1 2 3 4 5 6]

First row of b: [1 2 3]
Element at (1,2): 6
Slice of a[1:3]: [2 3]

Addition: [6 7 8 9]
Multiplication: [2 4 6 8]
Array Addition (a+a): [2 4 6 8]
Array Multiplication (a*a): [ 1  4  9 16]

Matrix Multiplication:
 [[19 22]
 [43 50]]
Elementwise Multiplication:
 [[ 5 12]
 [21 32]]
Transpose:
 [[1 3]
 [2 4]]

Square root: [1.         1.41421356 1.73205081 2.        ]
Exponent: [ 2.71828183  7.3890561  20.08553692 54.59815003]
Sine: [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
Mean: 2.5
Standard deviation: 1.118033988749895
Sum: 10
Max: 4
Min: 1

Condition (a > 2): [False False  True  True]
Elements > 2: [3 4]

Vertical Stack:
 [[1 2 3 4]
 [1 2 3 4]]
Horizontal Stack:
 [1 2 3 4 1 2 3 4]

Original a (modified): [100   2   3   4]
Copy c (unchanged): [1 2 3 4]
View v (reflects change): [100   2   3   4]
=== NumPy Slicing Examples (1D, 2D, 3D) ===

1D Array: [10 20 30 40 50 60]
Slice [1:4]: [20 30 40]
Slice [:3]: [10 20 30]
Slice [::2]: [10 30 50]
Slice [-3:]: [40 50 60]

2D Array:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]

First row: [10 20 30]
First column: [10 40 70]
Subarray (first 2 rows, first 2 cols):
 [[10 20]
 [40 50]]
Middle element: 50
Last column: [30 60 90]

Every other element in first row: [10 30]
Every other row:
 [[10 20 30]
 [70 80 90]]

3D Array:
 [[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
Shape: (2, 2, 3)

First block (index 0):
 [[1 2 3]
 [4 5 6]]
Second block (index 1):
 [[ 7  8  9]
 [10 11 12]]
First row of first block: [1 2 3]
Element at [1, 1, 2]: 12
All blocks, first row only:
 [[1 2 3]
 [7 8 9]]
All blocks, last column only:
 [[ 3  6]
 [ 9 12]]

Before modification:
 [[10 20 30]
 [40 50 60]
 [70 80 90]]

After modifying sub-slice:
Modified sub-slice:
 [[999  20]
 [ 40  50]]
Original array also changed (view behavior):
 [[999  20  30]
 [ 40  50  60]
 [ 70  80  90]]
 '''