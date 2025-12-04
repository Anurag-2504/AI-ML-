'''Q8. Let's create a Simple Calculator that performs arithmetic operations. Create
a function calculator(a, b, operation) that performs addition, subtraction,
multiplication, or division based on the operation parameter.'''

def calculator(num1,num2,operation):
    match operation:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1//num2
        case _:
            return "Invalid operation"

print(calculator(12,8,"+"))
print(calculator(12,8,"-"))
print(calculator(12,8,"*"))
print(calculator(12,4,"/"))
print(calculator(12,8,"%"))

'''
    Output:
    20
    4
    96
    3
    Invalid operation
'''
        