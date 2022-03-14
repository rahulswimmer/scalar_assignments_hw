class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self,prev_node,new_data):
        new_node = Node(new_data)

        if prev_node == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            if prev_node is None:
                return
                
            new_node.next = prev_node.next
            prev_node.next = new_node


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.push(0,65)
    llist.push(0,76)
    llist.push(2,88)

    llist.printList()

    