a = int(input("Enter start value:"))
b = int(input("Enter end value:"))

for num in range(a, b+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                print(num)
