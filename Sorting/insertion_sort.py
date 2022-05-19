"""
input = [6, 9, 1, 7, 12, 10]
output = [1, 6, 7, 9, 10, 12]

This is like arranging playing cards.

Pass-1:
1. Pick up first element (temp).
2. Is anything to the left of 6. No. So do nothing.
[6, 9, 1, 7, 12, 10]

Pass-2:
1. Pick up second element.
2. Is anything to the left of 9. Yes.
3. Is element before less than 9. Yes, it is 6. So do nothing.
[6, 9, 1, 7, 12, 10]

Pass-3:
1. Pick up third element.
2. Is anything to the left of 1. Yes.
3. Is element before less than 1. No, it is 9.
4. So move 9 to right and put temp there.
[6, 1, 9, 7, 12, 10]
5. Repeat 2-3-4.
[1, 6, 9, 7, 12, 10]
"""


class InsertionSort:
    def __init__(self, input):
        self.input = input

    def insertion_sort(self):
        for i in range(1, len(self.input)):
            temp = self.input[i]
            j = i-1
            while j >= 0:
                if temp < self.input[j]:
                    self.input[j+1] = self.input[j]
                    self.input[j] = temp
                j -= 1
            print('After cycle {0}, sorted list is: {1}'.format(i, self.input))
        return self.input


if __name__ == '__main__':
    input_list = [3, 1, 2]
    ins_sort = InsertionSort(input_list)
    result = ins_sort.insertion_sort()
    print('Final result is: ', result)
