def nth_maximum(num_list):
    """
    the function is for finding largest number
    :param num_list: integer list
    :return: maximum number
    """

    max_number = num_list[0]

    for x in num_list:
        if x > max_number:
            max_number = x

    return max_number


if __name__ == "__main__":
    num_align = [2,6,9,22,66]
    print(nth_maximum(num_align))


