import numpy as np

# =====================================================
# 1. CREATING NUMPY ARRAYS
# =====================================================

# Create a one-dimensional array
arr = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr)

# Create a two-dimensional array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D Array:")
print(arr2)

# Create arrays using built-in functions
print("\nZeros:", np.zeros(4))          # Array of four zeros
print("Ones:", np.ones(3))              # Array of three ones
print("Range:", np.arange(1, 6))        # Numbers from 1 to 5
print("Full:", np.full(3, 7))           # Array filled with 7


# =====================================================
# 2. ARRAY ATTRIBUTES
# =====================================================

print("\n--- Array Attributes ---")

print("Dimensions:", arr2.ndim)         # Number of dimensions
print("Shape:", arr2.shape)             # Rows and columns
print("Total Elements:", arr2.size)     # Total number of elements
print("Data Type:", arr2.dtype)         # Data type of elements


# =====================================================
# 3. INDEXING
# =====================================================

print("\n--- Indexing ---")

print("First Element:", arr[0])        # First element
print("Third Element:", arr[2])         # Third element
print("Last Element:", arr[-1])         # Last element

# Access an element using row and column
print("2D Element:", arr2[0, 1])        # Row 0, column 1


# =====================================================
# 4. SLICING
# =====================================================

print("\n--- Slicing ---")

print("Elements 1 to 3:", arr[1:4])     # Indices 1, 2, 3
print("First Three:", arr[:3])          # Start to index 2
print("From Index 2:", arr[2:])         # Index 2 to end
print("Every Second:", arr[::2])        # Every second element


# =====================================================
# 5. BASIC ARITHMETIC OPERATIONS
# =====================================================

print("\n--- Arithmetic Operations ---")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)               # Element-wise addition
print("Subtraction:", a - b)            # Element-wise subtraction
print("Multiplication:", a * b)         # Element-wise multiplication
print("Division:", a / b)               # Element-wise division
print("Power:", a ** 2)                 # Square each element

# Arithmetic with a single number (scalar)
print("Add Scalar:", a + 5)             # Add 5 to every element
print("Multiply Scalar:", a * 2)        # Multiply every element by 2


# =====================================================
# 6. MATHEMATICAL FUNCTIONS
# =====================================================

print("\n--- Mathematical Functions ---")

numbers = np.array([1, 4, 9, 16])

print("Square Root:", np.sqrt(numbers)) # Square root of each element
print("Sum:", np.sum(numbers))          # Sum of all elements
print("Mean:", np.mean(numbers))        # Average
print("Maximum:", np.max(numbers))      # Largest element
print("Minimum:", np.min(numbers))      # Smallest element
print("Standard Deviation:", np.std(numbers))  # Standard deviation
print("Sorted:", np.sort(numbers))      # Sort elements in ascending order


# =====================================================
# 7. COMPARISON OPERATIONS
# =====================================================

print("\n--- Comparison Operations ---")

print("Greater Than 20:", arr > 20)     # True where value > 20
print("Equal to 10:", arr == 10)        # True where value == 10


# =====================================================
# 8. BOOLEAN INDEXING / FILTERING
# =====================================================

print("\n--- Boolean Indexing ---")

# Select only elements greater than 25
result = arr[arr > 25]
print("Values Greater Than 25:", result)


# =====================================================
# 9. RESHAPING ARRAYS
# =====================================================

print("\n--- Reshaping ---")

numbers = np.array([1, 2, 3, 4, 5, 6])

# Convert 1D array into 2 rows and 3 columns
reshaped = numbers.reshape(2, 3)
print("Reshaped Array:")
print(reshaped)

# Convert into 3 rows and 2 columns
reshaped2 = numbers.reshape(3, 2)
print("Another Shape:")
print(reshaped2)


# =====================================================
# 10. CONCATENATION AND SPLITTING
# =====================================================

print("\n--- Concatenation and Splitting ---")

x = np.array([1, 2])
y = np.array([3, 4])

# Join two arrays into one
combined = np.concatenate((x, y))
print("Concatenated:", combined)

# Split six elements into three equal arrays
values = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(values, 3)
print("Split Arrays:", parts)


# =====================================================
# 11. MATRIX OPERATIONS
# =====================================================

print("\n--- Matrix Operations ---")

m1 = np.array([
    [1, 2],
    [3, 4]
])

m2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix Addition:")
print(m1 + m2)

print("Element-wise Multiplication:")
print(m1 * m2)

# @ performs matrix multiplication
print("Matrix Multiplication:")
print(m1 @ m2)


# =====================================================
# 12. COPYING ARRAYS
# =====================================================

print("\n--- Copying Arrays ---")

original = np.array([10, 20, 30])

# A simple assignment refers to the same array
reference = original
reference[0] = 99

print("Original After Assignment:", original)
print("Reference:", reference)

# copy() creates an independent array
original = np.array([10, 20, 30])
copied = original.copy()

copied[0] = 99

print("Original After Copy:", original)
print("Independent Copy:", copied)


# =====================================================
# END OF NUMPY BASIC OPERATIONS
# =====================================================
