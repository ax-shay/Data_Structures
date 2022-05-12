"""
Pseudo Code:

input = [3, 8, 1, 4, 2, 9, 6]
output = [1, 2, 3, 4, 6, 8, 9]

Pass-1:
1. min_index = 0, min_value = 3
2. iterate from index = 0+1..n and find & set a smaller value than min_value.
3. Swap (index=0, index=min_index)
--> output_1 = [1, 8, 3, 4, 2, 9, 6]

Pass-2:
1. min_index = 1, min_value = 8
2. iterate from index = 1+1..n and find & set a smaller value than min_value.
3. Swap (index=1, index=min_index)
--> output_2 = [1, 2, 3, 4, 8, 9, 6]

....
"""


class SelectionSort:
    def __init__(self, input_list):
        self.input_list = input_list

    def swap(self, i, min_index):
        self.input_list[i], self.input_list[min_index] = self.input_list[min_index], self.input_list[i]

    def selection_sort(self):
        for i in range(len(self.input_list)):
            min_index = i
            min_value = self.input_list[i]
            for j in range (i+1, len(self.input_list)):
                if self.input_list[j] < min_value:
                    min_value = self.input_list[j]
                    min_index = j
            self.swap(i, min_index)

        return self.input_list


if __name__ == '__main__':
    input_array = [3, 8, 1, 4, 2, 9, 6]
    ss = SelectionSort(input_array)
    print(ss.selection_sort())
