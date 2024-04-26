def calculate_emi(principal, rate, time):
    # Convert annual interest rate to monthly interest rate
    monthly_rate = rate / 12 / 100
    
    # Calculate EMI using the formula
    emi = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-time))

    return emi

def main():
    # Input principal amount, annual interest rate, and loan duration in years
    principal = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = int(input("Enter the loan duration in years: "))

    # Call the function to calculate EMI
    emi = calculate_emi(principal, rate, time)

    # Print the calculated EMI
    print("Your monthly EMI is: {:.2f}".format(emi))

if __name__ == "__main__":
    main()
