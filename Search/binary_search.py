"""
Time Complexity = O(log(n))

Recursion is generally slower in Python because it requires the allocation of new stack frames.
"""


class BinarySearch:
    def __init__(self):
        self.input_array = []

    def binary_search(self, elem):
        start = 0
        end = len(self.input_array) -1

        while start <= end:
            mid = (start + end) // 2
            if elem == self.input_array[mid]:
                return mid
            elif elem < self.input_array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


bi = BinarySearch()
bi.input_array = [10, 20, 30, 40, 50]
result = bi.binary_search(35)
print("Element Found at index {}".format(result) if result != -1 else "Element Not Found")
