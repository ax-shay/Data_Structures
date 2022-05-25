class MergeSort:
    def __init__(self):
        self.result = []

    def mergesort(self, arr):
        if len(arr) > 1:

            """Divide"""
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            self.mergesort(left)
            self.mergesort(right)

            """Merge"""
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr


if __name__ == '__main__':
    input_array = [3, 2, 1, 4, 0, -1]
    ms = MergeSort()
    print(ms.mergesort(input_array))
