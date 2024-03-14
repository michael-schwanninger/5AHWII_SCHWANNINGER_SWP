class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.data = data
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            old_node = self.head
            self.head = new_node
            new_node.next = old_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            item = self.head
            while item.next:
                item = item.next
            item.next = new_node

    def length(self):
        item = self.head
        count = 0
        while item:
            count += 1
            item = item.next
        return count

    def printList(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length():
            print("Index invalid!")
            return

        if index == 0:
            self.head = self.head.next
            return

        prev = self.head
        count = 0
        while prev:
            if count == index - 1:
                prev.next = prev.next.next
                break
            prev = prev.next
            count += 1


if __name__ == "__main__":
    linked_list = LinkedList(5)
    linked_list.insertAtBegin(10)
    linked_list.insertAtEnd(15)
    linked_list.insertAtEnd(25)
    #print(linked_list.length())
    linked_list.printList()
    print("\n")
    linked_list.deleteAtIndex(2)
    linked_list.printList()