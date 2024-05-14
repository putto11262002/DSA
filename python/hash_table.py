"""
Hash table is data stucture that maps keys to values for high efiiciency lookups.

There are serveral implementations of hash tables. 

A common implementation is an array of linked lists with a hash code function.
In this implementation, to insert a key, we do the following:
1. Compute the key's hash code, which will usually be an int or long.
2. Map the hash code to an index in the array. This can be done with hash code % array_length.
3. At this index, there is a linked list of keys and values. Store the key and value in this index. We use linked list to handle collisions.
To retrieve the key, we do the following:
1. Compute the hash code from the key.
2. Compute the index from the hash code.
3. Search through the linked list for the key. If the key is found, return the value.

An alternative implementantation can use a balanced binary tree. This gives us an O(log n) lookup time. 
This implementation is useful when we need to keep the keys in order.
"""


