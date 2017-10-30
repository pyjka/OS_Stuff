""" https://www.codewars.com/kata/52597aa56021e91c93000cb0 """

def move_zeros(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == 0 and array[i] is not False:
                array[j],array[i]=array[i],array[j]
    return array