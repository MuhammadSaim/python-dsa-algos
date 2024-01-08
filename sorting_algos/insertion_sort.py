
'''
A simple implementation of insertion sort
'''
def insertion_sort(array):

      for step in range(1, len(array)):

            key = array[step]
            j = step - 1

            while j >= 0 and key < array[j]:
                  array[j+1] = array[j]
                  j -= 1

            array[j + 1] = key


array = [9, 5, 1, 4, 3]
print(array)
insertion_sort(array)
print(array)