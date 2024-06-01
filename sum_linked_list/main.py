class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
    
    def __repr__(self):
        return self.value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __get_list(self):
        items = [self.head.value]
        node = self.head 
        while node.next is not None:
            node = node.next
            items.append(node.value)
        items.append(node.next)
        return items

    def __repr__(self):
        return " -> ".join([str(item) for item in self.__get_list()])

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head 
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node 


if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(8)

    
    breakpoint()
