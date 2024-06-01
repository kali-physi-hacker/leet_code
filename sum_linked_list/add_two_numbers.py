class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


class Solution:
    def get_values(self, list_node):
        values = [list_node.val]
        node = list_node
        while node.next is not None:
            node = node.next
            values.append(node.val)
        return values

    def create_list_node(self, values):
        value = values[0]
        node = ListNode(val=value)
        for value in values[1:]:
            next_node = ListNode(val=value)
            node.next = next_node
            node = next_node
        return node

        
    def addTwoNumbers(self, l1, l2):
        l1_values = self.get_values(l1)
        l1_values.reverse()
        l2_values = self.get_values(l2)
        l2_values.reverse()

        l1_reversed = int("".join([str(value) for value in l1_values]))
        l2_reversed = int("".join([str(value) for value in l2_values]))

        new_l = l1_values + l2_values
        new_l.reverse()
        
        result = self.create_list_node(values=new_l)

        return result


if __name__ == "__main__":
    l1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(5)
    l1.next = n2
    n2.next = n3

    l2 = ListNode(4)
    c1 = ListNode(6)
    c2 = ListNode(2)
    l2.next = c1
    c1.next = c2

    # breakpoint()
    Solution().addTwoNumbers(l1, l2)
    breakpoint()
