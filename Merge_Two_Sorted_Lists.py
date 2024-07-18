# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list 
# should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

def Merge_Two_Sorted_Lists(list1,list2):
    x = list1+list2
    x.sort()
    return x
print(Merge_Two_Sorted_Lists([1,3,3,4,5],[1,6,7,8,9]))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()  # Create a dummy node to simplify the merge process
    tail = dummy  # This will be the end of the merged list

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # At least one of list1 and list2 can still have nodes, attach the remaining nodes to tail
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next  # The merged list starts at dummy.next

# Helper function to convert list to linked list
def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
list1 = to_linked_list([1, 2, 4])
list2 = to_linked_list([1, 3, 4])
merged_list_head = mergeTwoLists(list1, list2)
print(to_list(merged_list_head))  # Output: [1, 1, 2, 3, 4, 4]

# Additional examples:
print(to_list(mergeTwoLists(to_linked_list([]), to_linked_list([]))))