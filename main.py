def find_smallest_int(arr):
    if len(arr) > 0:
        min_num = arr[0]
        for element in arr:
            if element < min_num:
                min_num = element
        return min_num
    else:
        return None







print(find_smallest_int( [34, 15, 88, 2, -1] ))