
def Power_of_2(power):
    result = 1
    for i in range(1, power + 1):
        result = result * 2
    return result


if __name__=="__main__":
    power = 4
    print(Power_of_2(power))