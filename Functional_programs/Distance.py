import math


def euclidean_distance(x, y):
    """
    function to calculate euclidean distance from point (x,y) to origin (0,0)
    :param x:first coordinate value
    :param y:second coordinate values
    :return:distance from origin
    """
    if x == 0 and y == 0:
        print("distance is zero")
    else:
        distance = math.sqrt(x**x + y**y)
        print("The distance is: ", distance)


if __name__ == "__main__":
    x1 = int(input("First coordinate value: "))
    y1 = int(input("second coordinate value: "))
    euclidean_distance(x1, y1)