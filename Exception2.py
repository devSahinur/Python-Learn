# multiple Exception how to work

try:
    num1 = int(input("Enter First Number :"))
    num2 = int(input("Enter Second Number :"))
    result = num1 / num2
    print(result)
except (ValueError, ZeroDivisionError):
    print("you have entered incorrect innput.")

finally:
    print("Thanks !!!")
