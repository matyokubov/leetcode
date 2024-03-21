#Input
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#Logic
def main(list1, list2):
    # Helper function
    def makeLinkedList(*items):
        head = ListNode(items[0])
        current = head
        for i in items[1:]:
            t = ListNode(i)
            current.next = t
            current = t
        return head

    #Unpack items to 'arr'
    arr = []
    current = list1
    while current!=None:
        arr.append(current.val)
        current = current.next
    current = list2
    while current!=None:
        arr.append(current.val)
        current = current.next
        
    # I didn't know how to solve the problem without built-in sorted.
    r = sorted(arr)
    if len(r)!=0:
        return makeLinkedList(*r)
    return ListNode().next
    
#Output
#res = main(list1, list2)
#print(res)

