#Calculator Project - Brooke Comstock
#Allow the user to input 2 numbers and a desired operator, and obtain the correct result.
#Test each operation function within the calculator to ensure each is working properly.

#import math module
import math

#Ask the user for the first number they wish to work with and assign the input globally
Num1 = input("Input your first number: ")
#Ask the user for their desired operation and asssign it to a variable to be evaluated within the function
Operator = input("Input desired operation: ")
#Ask the user for the second number they wish to work with and assign the input globally
Num2 = input("Input your second number: ")

#Converting their input to float numbers and assigning them to variables globally.
#Some operations require that the input is in float form, so by defining the variable globally in this way, we can ensure all run smoothly.
Num1 = float(Num1)
Num2 = float(Num2)

#Create the calculator function
def calculator(Num1, Num2, Operator):
    
    #Evaluating the operator to complete the correct task using an "if" and many "elif" statements
    if Operator == "+":
        #Add Num1 and Num2
        answer = (Num1 + Num2)
    elif Operator == "-":
        #Subtract Num2 from Num1
        answer = (Num1 - Num2)
    elif Operator == "/":
        #Divide Num1 by Num2
        answer = (Num1 / Num2)
    elif Operator == "//":
        #Divide Num1 by Num2 and return the integer quotient
        answer = (Num1 // Num2)
    elif Operator == "%":
        #Divide Num1 by Num2 and return the remainder
        answer = (Num1 % Num2)
    elif Operator == "*":
        #Multiply Num1 by Num2
        answer = (Num1 * Num2)
    elif Operator == "**":
        #Raise Num1 to the power of Num2
        answer = (Num1**Num2)
    #Bonus operations: trigonometric function and copy sign using the math module
    elif Operator == "tan":
        #Returns atan(Num1 / Num2), in radians
        answer = math.atan2(Num1, Num2)
    elif Operator == "copy sign":
        #Return a float with the magnitude (absolute value) of Num1 but the sign of Num2
        answer = math.copysign(Num1, Num2)
    else: 
        #Catch-all else. Function will define the answer variable this way if the function does not fall under one of our if/elif statements.
        answer = "Unrecognized function, try again."
    #By defining the same variable name "answer" for each operator output, we only require one return function, making for cleaner code.
    return(f"Calculator output: {answer}")

#Finally, printing our function.
print(calculator(Num1, Num2, Operator))

#Testing:
def test_calc():
    #Test that the addition operation works correctly, the result should be the exact statement recalled below.
    #If the calculator function output does not match the expected result, the following statement will print; stating what the calculator was expected to produce versus what it did.
    result = calculator(3,4,"+")
    assert result == f"Calculator output: 7", f"Expected output: 7, {result}"
    #Test the accuracy of the subraction operation.
    result = calculator(89.5,80.0,"-")
    assert result == f"Calculator output: 9.5", f"Expected output: 9.5, {result}"
    #Test the division operation.
    result = calculator(5,2,"/")
    assert result == f"Calculator output: 2.5", f"Expected output: 2.5, {result}"
    #Test the floor division operation, noting it will return in int form.
    result = calculator(10,1,"//")
    assert result == f"Calculator output: 10", f"Expected output: 10, {result}"
    #Test the modulus operation, noting it returns in int form.
    result = calculator(33,2,"%")
    assert result == f"Calculator output: 1", f"Expected output: 1, {result}"
    #Test the multiplication operation.
    result = calculator(89,.5,"*")
    assert result == "Calculator output: 44.5", f"Expected output: 44.5, {result}"
    #Test the power function, noting it returns in floats.
    result = calculator(25,.5,"**")
    assert result == "Calculator output: 5.0", f"Expected output: 5.0, {result}"
    #TEST BONUSES
    #Testing the tan function.
    result = calculator(1,1,"tan")
    assert result == "Calculator output: 0.7853981633974483", f"Expected output:0.7853981633974483, {result}"
    #testing the copysign function, noting that it returns answers as floats.
    result = calculator(1.0,-10,"copy sign")
    assert result == "Calculator output: -1.0", f"Expected output: -1.0, {result}"
test_calc()







    