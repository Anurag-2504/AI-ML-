'''
    Q9. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
        compute simple interest:
'''

P = float(input("Enter the Principal amount (P): "))
R = float(input("Enter the Rate of interest (R): "))
T = float(input("Enter the Time period in years (T): "))
simple_interest = (P * R * T) / 100
print("The Simple Interest is:", simple_interest)
print("Total  amount after", T, "years is:", P + simple_interest)
