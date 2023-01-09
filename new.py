def sum():
        a = (input("Enter number1 : "))
        b = (input("enter number2 : "))
        try:
            sum = a+b
            return sum
        except ValueError:
            return("Input Value error")



print(sum())
