class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printlist(self):

        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next


#if __name__ == 'main':

llist = LinkedList()
llist.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)


llist.head.next = second
second.next = third
third.next = fourth
llist.printlist()