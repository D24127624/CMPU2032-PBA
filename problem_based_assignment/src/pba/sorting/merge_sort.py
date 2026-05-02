from ..patient_records import LinkNode, PatientRecords


class MergeSort:

    def __init__(self, patient_records: PatientRecords, key: str):
        self.patient_records = patient_records
        self.key = key

    def sort(self):
        '''Perform the sorting on the parient records linked-list.'''

        node = self.__merge_sort(self.patient_records.head)
        self.patient_records.head = self.patient_records.tail = node
        while node is not None and node.next is not None:
            self.patient_records.tail = node.next
            node = node.next

    def __merge_sort(self, node: LinkNode):
        '''Execute the sorting of the provided records using merge sort algorithm.'''

        # if the list is empty
        if node is None:
            return None
        # if the list only has one element
        elif node.next is None:
            return node
        # split the list into two halves and sort each half recursively
        middle = self.__get_middle(node)
        next = middle.next
        middle.next = None

        left = self.__merge_sort(node)
        right = self.__merge_sort(next)

        return self.__do_merge(left, right)

    def __do_merge(self, left, right):
        '''Sort the values in the left and right lists and merge them together.'''

        # return either the left or right list of the other is empty
        if left is None:
            return right
        elif right is None:
            return left

        result = None
        if self.__get_value(left) < self.__get_value(right):
            result = left
            result.next = self.__do_merge(left.next, right)
        else:
            result = right
            result.next = self.__do_merge(left, right.next)
        return result

    def __get_middle(self, node):
        '''Helper method to get the middle node of the linked list.'''

        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __get_value(self, node: LinkNode):
        '''Helper method to get the node data for comparison.'''

        return getattr(node.data, self.key)
