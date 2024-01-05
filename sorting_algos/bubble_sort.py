'''
      a simple implementation of the bubble sort on an array
'''
def bubble_sort(list: list):

      '''
      loop through to access each element of an list
      Suppose we have list [-2, 45, 0, 11, -9]
      this loop will loop through the outer array
      '''
      for i in range(len(list)):

            '''
            On first loop we having 1 in an i
            after the calculation of th range
            range = list size - i - 1 => i=1
            range = 5 - 1 - 1
            range = 3
            and j = 0
            now check  list[j] => list[0] = 0 and list[j+1] => list[1]
            compare those if j is less the j+1 then swap and continue
            '''
            for j in range(0, len(list) - i - 1):

                  if list[j] > list[j + 1]:
                        tmp = list[j]
                        list[j] = list[j+1]
                        list[j+1] = tmp


list = [-2, 45, 0, 11, -9]
print(list)
bubble_sort(list)
print(list)