"""
Arrays
- Arrays are used to store a list of elements of the same data type.
- Arrays are fixed in size.


Resizing Arrays
- It is ussually useful to have a resizable array, which is an array that can grow or shrink in size.
- Insertions to resizable array has an amortized time complexity of O(1).


Why use string builder
- Strings are usually immutable in many languages, meaning that they cannot be changed after they are created.
- This means that when we concatanate strings, we are actually creating a new string and copy the original strings over.
- This can be inefficient if we are concatanating many strings together.
- To solve this problem, we can use a string builder, which is a resizable array of strings.
"""

