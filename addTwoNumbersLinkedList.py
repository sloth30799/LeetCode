# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def linked_list_val(l: Optional[ListNode]) -> str:
        val = ''

        while (l.val or l.val == 0):
            val += str(l.val)

            if (l.next):
                l = l.next
            else:
                break

        return val[::-1] if val else '0'

    l1_val = int(linked_list_val(l1))
    l2_val = int(linked_list_val(l2))

    result = str(l1_val + l2_val)[::-1]

    head = ListNode(int(result[0]))
    current = head

    for r in result[1:]:
        current.next = ListNode(int(r))
        current = current.next

    return head
