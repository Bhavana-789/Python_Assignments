def EvenOrOdd():
    num = int(input("Enter a number to check if it is even or odd:"))
    if(num%2==0):
        print(num,"it is a even number")
    else:
        print(num,"it is odd number")
        return num

if __name__=="__main__":
    EvenOrOdd()