#Defining functions
#Add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

#Dictionary to serve as the means to how we call the functions
# ex./ function = operations[key]
#      function(2,3)
operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():
    #Ask user for first number
    num1 = float(input("What's the first number? "))

    #print out operations and ask user for what they want to do
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        selected_operation = str(input("Pick an operation: "))
        num2 = float(input("What's the next number? "))

        #call function from dictionary, pass numbers-->dictionary[key_for_function](arg1,arg2)
        answer = operations[selected_operation](num1,num2)

        print(f"{num1} {selected_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            #recursive call -- if we end the while loop, then call the calculator function, basically telling the computer to start from the beginning
            #need to make sure whenusing recurssion that there is a switch to toggle in while loop
            calculator()

#call function to begin the program
calculator()