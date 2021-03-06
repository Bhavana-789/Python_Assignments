#import pytest
def monthly_payment(y, p, r):
    """
    function for calculating monthly payment
    :param y: year to pay
    :param p: principal loan amount
    :param r: per cent interest monthly
    :return: payment as per formula
    """
    n = 12 * y
    R = r / (12*100)

    payment = (p*R)/(1-(1+R)**(-n))

    return payment

def test_my_func():
    assert monthly_payment(2, 200000, 2) == 8508.052673695847




if __name__ == "__main__":
    output = monthly_payment(2, 200000, 2)
    print(output)