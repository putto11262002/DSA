

def insert(m: int, n: int, i: int, j: int) -> int: 
    all_ones = ~0
    left = all_ones << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted

res = insert(0b10011, 0b10000000000, 2, 6)
print(bin(res))


































"""

    You are given two 32-bit numbers, n and m, and two bit positions, i and j. Write a method to insert m into n such that m starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of m. That is, if m = 10011, you can assume that there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because m could not fully fit between bit 3 and bit 2.

    # Create a mask to clear bits i through j in n. 
    # Example: i = 2, j = 4. Result should be 11100011. For simplicity, we'll use just 8 bits for the example. 
    # n = 11111111
    # 1. Shift 1 over by j bits. 1 << 4 = 00010000
    # 2. Subtract 1 from the result to get a sequence of 1s. (1 << 4) - 1 = 00001111
    # 3. Shift this sequence left by i bits. (1 << 4) - 1 << 2 = 00001100
    # 4. Invert this mask. 
    # 5. AND this mask with n. 
    all_ones = ~0
    left = all_ones << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted
"""