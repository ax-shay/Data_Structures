class InsertionSort:
    def __init__(self):
        self.input_array = []

    def insertion_sort(self):
        for i in range(1, len(self.input_array)):
            val = self.input_array[i]
            pos = i
            while pos > 0:
                if self.input_array[pos] < self.input_array[pos - 1]:
                    self.input_array[pos] = self.input_array[pos - 1]
                    self.input_array[pos - 1] = val
                pos -= 1
            print("Sorted array after {0} pass is: {1}".format(i, self.input_array))
        return self.input_array


ins = InsertionSort()
ins.input_array = [5, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
result = ins.insertion_sort()
print("Finally, Sorted Array is: " + str(result))
