def append(self, after_val, val):
        # Input => (3->6->1->7->2->None, 6, 4)
        # Output => 3->6->4->1->7->2->None
        runner = self.head
        while runner is not None:
            if runner.val == after_val:
                next_node = runner.next
                runner.next = Node(val)
                runner.next.next = next_node
                return self
            runner = runner.next
        print('no node with val=' + str(after_val) + ' found in SLL')
        return self
def delete(self, val):
        # Input => 3->6->1->7->2->None, 1
        # Output => # 3->6->7->2->None
        runner = self.head
        prev = runner
        if runner.val == val:
            self.head = runner.next
        while runner is not None:
            if runner.val == val:
                prev.next = runner.next
                return self
            prev = runner
            runner = runner.next
        print('no node with val=' + str(val) + ' found in SLL')
        return self
