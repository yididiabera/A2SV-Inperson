class Node:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next
    def __str__(self):
        arr  = [str(self.value)]
        node = self.next
        while node:
            arr.append(str(node.value))
            node = node.next
        return '->'.join(arr)

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        #print("get", self.dummy)
        temp = self.dummy.next
        i = 0
        while temp:
            if i == index:
                return temp.value
            temp = temp.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        #print("addhead", self.dummy)
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        
    def addAtTail(self, val: int) -> None:
        #print("addtail", self.dummy)
        new_node = Node(val)
        temp = self.dummy  #why not self.dummy.next
        # if not temp:
        #     self.dummy.next = new_node
        #     return

        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        #print("addidx", self.dummy)
        new_node = Node(val)
        temp = self.dummy.next
        i = 0

        if index == 0:
            self.addAtHead(val)
            return

        while temp and i < index - 1:
            temp = temp.next
            i += 1
        
        if temp:
            new_node.next = temp.next
            temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        #print("delete", self.dummy)
        temp = self.dummy.next
        if index == 0:
            if self.dummy.next:
                self.dummy.next = self.dummy.next.next
            return

        i = 0
        while temp and i < index - 1:
            temp = temp.next
            i += 1
        if temp and temp.next:
            temp.next = temp.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)