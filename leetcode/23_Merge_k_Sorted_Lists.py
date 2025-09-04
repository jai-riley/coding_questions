# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or len(lists) == 0:
            return None
        indices = [0] * len(lists)
        finished = [0] * len(lists) 
        merged = ListNode()
        answer = merged
        while len(lists) > 0:
            min_so_far = []
            for a in range(len(lists)):
                if finished[a] == 0 and lists[a]:
                    if len(min_so_far) == 0:
                        min_so_far.append(lists[a].val)
                        min_so_far.append(a)
                    elif lists[a].val < min_so_far[0]:
                        min_so_far[0] = lists[a].val
                        min_so_far[1] = a
            if min_so_far:
                merged.next = ListNode(min_so_far[0])
                merged = merged.next
                lists[min_so_far[1]] = lists[min_so_far[1]].next
                if not lists[min_so_far[1]]:
                    lists.remove(lists[min_so_far[1]])
            else:
                lists = []
        return answer.next

