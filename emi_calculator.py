
def calculate_emi(principal, annual_rate, years):

    # Convert annual interest rate to monthly decimal rate
    monthly_rate = annual_rate / (12 * 100)

    # Convert tenure into number of monthly instalments
    months = years * 12

    # Handle zero-interest loans
    if monthly_rate == 0:
        return principal / months

    # Calculate EMI using reducing-balance formula
    emi = (
        principal * monthly_rate *
        (1 + monthly_rate) ** months
    ) / (
        (1 + monthly_rate) ** months - 1
    )

    return emi


# Test with three different customers

customers = [
    {"name": "Customer A", "principal": 500000, "rate": 10, "years": 5},
    {"name": "Customer B", "principal": 1000000, "rate": 12, "years": 10},
    {"name": "Customer C", "principal": 2000000, "rate": 8.5, "years": 15}
]

for customer in customers:

    emi = calculate_emi(
        customer["principal"],
        customer["rate"],
        customer["years"]
    )

    months = customer["years"] * 12
    total_payment = emi * months
    total_interest = total_payment - customer["principal"]

    print("\n", customer["name"])
    print("Monthly EMI:", round(emi, 2))
    print("Total Repayment:", round(total_payment, 2))
    print("Total Interest:", round(total_interest, 2))
