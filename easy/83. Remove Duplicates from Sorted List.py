class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#Input
def makeLinkedList(*items):
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        t = ListNode(item)
        current.next = t
        current = t
    return head
head = makeLinkedList(1, 1, 2, 3, 3)
        
#Logic
def main(head):
    '''
    There's no difference between:
        while current and current.next
        while current.next and current
    But in leetcode, this condition is wrong:
        while current.next and current
    '''
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

#Output
def extractLinkedList(head):
        t = []
        current = head
        while current!=None:
            t.append(current.val)
            current = current.next
        return t
        
res = main(head)
print(extractLinkedList(res))
