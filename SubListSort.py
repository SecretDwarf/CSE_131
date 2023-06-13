def test_sub_list_sort():
    # test cases
    array1 = [31, 72, 32, 10, 95, 50, 25, 18]
    expected1 = [10, 18, 25, 31, 32, 50, 72, 95]
    assert sub_list_sort(array1) == expected1, "Test case 1 failed!"

    array2 = [5, 4, 3, 2, 1]
    expected2 = [1, 2, 3, 4, 5]
    assert sub_list_sort(array2) == expected2, "Test case 2 failed!"

    array3 = [1]
    expected3 = [1]
    assert sub_list_sort(array3) == expected3, "Test case 3 failed!"

    array4 = []
    expected4 = []
    assert sub_list_sort(array4) == expected4, "Test case 4 failed!"

    array5 = [10, 20, 30, 40, 50]
    expected5 = [10, 20, 30, 40, 50]
    assert sub_list_sort(array5) == expected5, "Test case 5 failed!"

    array6 = [5, 2, 8, 3, 2, 1, 5, 4, 3]
    expected6 = [1, 2, 2, 3, 3, 4, 5, 5, 8]
    assert sub_list_sort(array6) == expected6, "Test case 6 failed!"

    array7 = [9, 7, 5, 3, 1]
    expected7 = [1, 3, 5, 7, 9]
    assert sub_list_sort(array7) == expected7, "Test case 7 failed!"

    array8 = [-3, 0, -5, 2, -1, 4]
    expected8 = [-5, -3, -1, 0, 2, 4]
    assert sub_list_sort(array8) == expected8, "Test case 8 failed!"

    array9 = [1, 2, 3, 4, 4, 3, 2, 1]
    expected9 = [1, 1, 2, 2, 3, 3, 4, 4]
    assert sub_list_sort(array9) == expected9, "Test case 9 failed!"

    array10 = [100, 50, 200, 150, 300, 250, 400, 350, 500, 450]
    expected10 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    assert sub_list_sort(array10) == expected10, "Test case 10 failed!"
    
    array11 = [3, 3, 3, 3, 3]
    expected11 = [3, 3, 3, 3, 3]
    assert sub_list_sort(array11) == expected11, "Test case 11 failed!"

    array12 = [5, 4, 3, 2, 1, 0, -1, -2, -3]
    expected12 = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert sub_list_sort(array12) == expected12, "Test case 12 failed!"

    print("All test cases passed!")

def sub_list_sort(array):
    # Check if the array is already sorted
    if array == sorted(array):
        return array

    src = array[:]
    size = len(src)
    dest = [0] * size
    num = 2

    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1

            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
                while end2 < size and src[end2 - 1] <= src[end2]:
                    end2 += 1

            num += 1
            combine(src, dest, begin1, end1, begin2, end2)
            begin1 = end2

        src, dest = dest, src

    return src

def combine(source, destination, begin1, end1, begin2, end2):
    i = begin1

    while i < end2:
        if begin1 < end1 and (begin2 == end2 or begin1 < len(source) and source[begin1] <= source[begin2]):
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1
        i += 1

# Run the tests
test_sub_list_sort()
