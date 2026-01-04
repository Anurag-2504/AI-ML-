'''
    Q7. Ask the user for a temperature in Celsius (string input). Convert it to float ,
        then calculate and print temperature in Fahrenheit.
'''
temp_celsius = input("Enter temperature in Celsius: ")
temp_celsius_float = float(temp_celsius)
temp_fahrenheit = (temp_celsius_float * 9/5) + 32
print("Temperature  in Fahrenheit:", temp_fahrenheit)