'''Q10. Take a decimal number as input (like 45.78 ) and output its: • 
   integer part - 45
    fractional part - . 78
'''
decimal_number = float(input("Enter a decimal number: "))
interger_part = int(decimal_number)
fractional_part = decimal_number - interger_part
print("Integer part:", interger_part)
print("Fractional  part:", fractional_part)
