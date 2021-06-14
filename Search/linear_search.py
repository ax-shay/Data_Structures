"""
Time Complexity = O(n)
"""


class LinearSearch:
    def __init__(self):
        self.input_array = []

    def linear_search(self, elem):
        for i in range(0, len(self.input_array)):
            if elem == self.input_array[i]:
                return i
        return -1


ls = LinearSearch()
ls.input_array = [1, 2, 3, 4, 5, 2, 1, 20]
result = ls.linear_search(5)
print("Element found at index pos: {0}".format(result) if result != -1 else "Element Not Found")
