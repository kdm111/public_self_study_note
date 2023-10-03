
class ListNode:
    def __init__(self, val):
        self.val  = val
        self.next = None

def printNodes(node : ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=" ")
        crnt_node = crnt_node.next
    print()

class SLinkedList:
    def __init__(self):
        self.head = None

    def addHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    def addBack(self, val):
        node = ListNode(val)
        crnt_node = self.head
        if crnt_node:
            while crnt_node.next:
                crnt_node = crnt_node.next
            crnt_node.next = node

slist = SLinkedList()
# slist.addHead(2)
slist.addBack(1)
printNodes(slist.head)


