class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0

        v1, v2 = ListNode(-1, l1), ListNode(-1, l2)
        pp1, pp2 = v1, v2
        p1, p2 = l1, l2
        while p1 and p2:
            # print(v1)
            cur_sum = p1.val + p2.val + flag
            p1.val = cur_sum % 10
            flag = cur_sum // 10

            pp1 = p1
            pp2 = p2
            p1 = p1.next
            p2 = p2.next

        if p1 is None:
            pp1.next = p2
            while p2:
                cur_sum = p2.val + flag
                p2.val = cur_sum % 10
                flag = cur_sum // 10

                pp1 = p2
                p2 = p2.next
        elif p2 is None:
            while p1:
                cur_sum = p1.val + flag
                p1.val = cur_sum % 10
                flag = cur_sum // 10

                pp1 = p1
                p1 = p1.next

        if flag:
            pp1.next = ListNode(flag)

        return v1.next