# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # dummy = ListNode(0)
        # tail = dummy
        # while True:
        #     mini = -1
        #     for i in range(len(lists)):
        #         if lists[i] is not None:
        #             if mini == -1 or lists[i].val < lists[mini].val:
        #                 mini = i
        #     if mini == -1:
        #         break
        #     tail.next = lists[mini]
        #     tail = tail.next
        #     lists[mini] = lists[mini].next
        # return dummy.next
        a = []
        dummy = ListNode(0)
        tail = dummy
        for i in lists:
            while i:
                a.append(i.val)
                i = i.next
        for i in sorted(a):
            tail.next = ListNode(i)
            tail = tail.next
        return dummy.next
        

                    
