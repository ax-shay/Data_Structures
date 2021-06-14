"""
Time Complexity = O(n^2)
Space Complexity = O(1)
"""


class BubbleSort:
    def __init__(self):
        self.input_array = []

    def _sort(self, ind):
        self.input_array[ind], self.input_array[ind+1] = self.input_array[ind+1], self.input_array[ind]

    def bubble_sort(self):
        has_swapped = True
        iterator = 0

        while has_swapped:
            has_swapped = False

            for i in range(len(self.input_array) - iterator - 1):
                if self.input_array[i] > self.input_array[i+1]:
                    self._sort(i)
                    has_swapped = True
            iterator += 1
            print("Array at the end of {0} pass is: {1}".format(iterator, self.input_array))
        return self.input_array


a = BubbleSort()
a.input_array = [14, 46, 43, 27, 57, 50, 41, 45, 21, 7]
sorted_array = a.bubble_sort()
print("Finally, Sorted Array is: " + str(sorted_array))

