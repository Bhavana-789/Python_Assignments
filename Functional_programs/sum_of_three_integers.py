def triplets(arr, arr_len, Sum):
    """
    function to find sum of three integers that adds to 0
    :param arr: contains array elements
    :param arr_len: for length of array
    :param Sum: to calculate no of triplets that sum to 0
    :return: all possible triplets
    """
    for i in range(0, arr_len-2):
        for j in range(i+1, arr_len-1):
            for k in range(j+1, arr_len):
                if(arr[i] + arr[j] + arr[k] == Sum):
                    print(arr[i], arr[j], arr[k])


if __name__ =="__main__":
    arr_values = [2, 5, -4, 7, 3, -3]
    arr_length = len(arr_values)
    Sum1=0
    print("All possible triplets are: ")
    triplets(arr_values, arr_length, Sum1)






