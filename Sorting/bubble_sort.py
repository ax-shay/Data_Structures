"""
input = [3, 8,  9, 4, 7, 1]
output = [1, 3, 4, 7, 8, 9]

Pass-1:
1. if 1 < 7, Swap (input[n], input[n-1] = input[n-1], input[n]) [3, 8, 9, 4, 1, 7]
2. if 1 < 4, Swap (input[n-1], input[n-2] = input[n-2], input[n-1]) [3, 8, 9, 1, 4, 7]
3. if 1 < 9, Swap (input[n-2], input[n-3] = input[n-3, input[n-2]) [3, 8, 1, 9, 4, 7]
4. if 1 < 8, Swap (input[n-3], input[n-4] = input[n-4, input[n-3]) [3, 1, 8, 9, 4, 7]
5. if 1 < 3, Swap (input[n-4], input[n-5] = input[n-5, input[n-4]) [1, 3, 8, 9, 4, 7]

Pass-2:
1. if 7 < 4, [1, 3, 8, 9, 4, 7]
2. if 4 < 9, Swap (input[n-1], input[n-2] = input[n-2], input[n-1]) [1, 3, 8, 4, 9, 7]
3. if 4 < 8, Swap (input[n-2], input[n-3] = input[n-3, input[n-2]) [1, 3, 4, 8, 9, 7]
4. if 4 < 3, [1, 3, 4, 8, 9, 7]

..
"""


class BubbleSort:
    def __init__(self, input):
        self.input = input

    def _swap(self, j):
        self.input[j], self.input[j-1] = self.input[j-1], self.input[j]

    def bubble_sort(self):
        for i in range(0, len(self.input)-1):
            for j in range(len(self.input)-1, i, -1):
                if self.input[j] < self.input[j-1]:
                    self._swap(j)
        return self.input


if __name__ == '__main__':
    input_list = [3, 8,  9, 4, 7, 1]
    bubble = BubbleSort(input_list)
    print(bubble.bubble_sort())
