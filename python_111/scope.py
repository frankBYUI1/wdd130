# Global variable
operator = "/"
 
def main():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    operator = input("Enter an operator: ")
    calc_value = do_simple_math(num1, num2)
    print(calc_value)
    
    calc_value = do_simple_math(num1, num2, operator)
    print(calc_value)
 
def do_simple_math(num1, num2, operator="+"):
    """
        Compute simple math equations
        parameters: num1, num2, operator (string)
    """
    computed_value = 0
    if operator == "+":
        computed_value = num1 + num2
    elif operator == "-":
        computed_value = num1 - num2
    elif operator == "*":
        computed_value = num1 * num2
    elif operator == "/":
        computed_value = num1 / num2
 
    return computed_value

main()