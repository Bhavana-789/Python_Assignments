def multiple_values(str, k):

    string = []

    sentence = str.split(" ")
    for x in sentence:
        if len(x) > k:
            string.append(x)
    return string


if __name__ == "__main__":
    str_value = "Welcome to Bridgelabz"
    j = 2
    print(multiple_values(str_value, j))
