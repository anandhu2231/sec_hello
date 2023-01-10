def sum():
        operation = input("select - int, float, others - ")
        if operation == "int":
            a = int(input("Enter number1 : "))
            b = int(input("enter number2 : "))
            sum = a+b
            return sum
        elif operation == "float":
            a = float(input("Enter number1 : "))
            b = float(input("enter number2 : "))    
            sum = a+b
            return sum
        elif operation == "other":
            a = str(input("Enter number1 : "))
            b = str(input("enter number2 : "))
            return a+b
        else:
            return "Wrong input"    






print(sum())
