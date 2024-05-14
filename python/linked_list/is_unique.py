import linked_list
from typing import Callable

"""
Prints the input list and the output list
"""
def test(test_case: 'list[int]', fn: Callable[[linked_list.Node], linked_list.Node]): 
    head = linked_list.gen_linked_list_from_list(test_case)
    print("Pre:  ", linked_list.to_string(head))
    head = fn(head)
    print("Post: ", linked_list.to_string(head))

"""
Is Unique

Bruteforce solution: 

- For each element in the list, compare it with all other elements after it.
- If if duplicated element it found remove it from the list.
- Time complexity: O(N^2)
- Space complexity: O(1)

"""


    

def remove_duplicates(head: linked_list.Node): 
    cur = head
    while cur is not None: 

        # Compare cur to the rest of the nodes values
        runner = cur
        while runner.next is not None: 
            if cur.val == runner.next.val: 
                runner.next = runner.next.next
            else: 
                runner = runner.next

        # Move the cur pointer to the next node
        cur = cur.next
    return head


test_1 = [5, 23, 7, 8, 3, 7, 23, 23, 23]
test_2 = [26, 3, 8, 9]
test(test_case=test_1, fn=remove_duplicates)

test(test_case=test_2, fn=remove_duplicates)

"""
It is not necessary for us to seach the linked list every time to find deplicates. 
We can track what we have already seen in the list, and for each node we just have to check if we have already seen it. 
We can use a hashmap to store the seen values, as hashmap has O(n) look up time. 
This optimization has brought the time complexity of the algorithm down to O(N) while suffering a space complexity of O(N).
"""

def remove_duplcates_v2(head: linked_list.Node): 
    seen = set()
    runner = head
    prev = None

    while runner is not None:
        if runner.val in seen: 
            prev.next = runner.next
        else: 
            seen.add(runner.val)
            prev = runner
        runner = runner.next
    
    return head


test(test_1, remove_duplcates_v2)
test(test_2, remove_duplcates_v2)











            
    
    