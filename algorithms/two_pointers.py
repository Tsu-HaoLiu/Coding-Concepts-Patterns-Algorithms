
def two_pointers(array):

    start = 0
    end = len(array) - 1

    while start != end:

        if array[start] != array[end]:
            return False

        start += 1
        end -= 1
    return True


nums1 = [1,2,3,0,0,0]

nums1.insert()

array1 = 'supercalifragilisticexpialidocious'
print(two_pointers(array1) == False)

array2 = 'racecar'
print(two_pointers(array2) == True)
