def leap_year(year):
     if 999 < year < 10000:
         result= year % 400 == 0 or year % 4 == 0 and year % 100 !=0
         print(result)
     else:
         print("Enter four digit number")

if __name__=="__main__":
    y = int(input("Enter a year"))
    leap_year(y)