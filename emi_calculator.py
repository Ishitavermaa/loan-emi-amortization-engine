
import math


# --------------------------------------------------
# STEP 1: EMI CALCULATION FUNCTION
# --------------------------------------------------

def calculate_emi(principal, annual_rate, years):

    # Validate input types
    if isinstance(principal, bool) or not isinstance(principal, (int, float)):
        raise TypeError("Loan amount must be a number.")

    if isinstance(annual_rate, bool) or not isinstance(annual_rate, (int, float)):
        raise TypeError("Interest rate must be a number.")

    if isinstance(years, bool) or not isinstance(years, int):
        raise TypeError("Loan tenure must be a whole number of years.")

    # Validate input values
    if not math.isfinite(principal) or principal <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    if not math.isfinite(annual_rate) or annual_rate < 0:
        raise ValueError("Interest rate cannot be negative or infinite.")

    if years <= 0:
        raise ValueError("Loan tenure must be greater than zero.")

    # Convert annual interest rate into monthly decimal rate
    monthly_rate = annual_rate / (12 * 100)

    # Convert years into number of monthly instalments
    months = years * 12

    # Handle zero-interest loans
    if monthly_rate == 0:
        return principal / months

    # Calculate EMI using reducing-balance formula
    rate_factor = (1 + monthly_rate) ** months

    emi = (
        principal * monthly_rate * rate_factor
    ) / (
        rate_factor - 1
    )

    return emi


# --------------------------------------------------
# STEP 2: CUSTOMER LOAN DATA
# --------------------------------------------------

customers = [
    {
        "name": "Customer A",
        "principal": 500000,
        "annual_rate": 10,
        "years": 5
    },
    {
        "name": "Customer B",
        "principal": 1000000,
        "annual_rate": 12,
        "years": 10
    },
    {
        "name": "Customer C",
        "principal": 2000000,
        "annual_rate": 8.5,
        "years": 15
    }
]


# --------------------------------------------------
# STEP 3: CALCULATE AND DISPLAY LOAN DETAILS
# --------------------------------------------------

print("=" * 55)
print("             LOAN EMI CALCULATOR")
print("=" * 55)

for customer in customers:

    name = customer["name"]
    principal = customer["principal"]
    annual_rate = customer["annual_rate"]
    years = customer["years"]

    try:
        # Calculate EMI
        emi = calculate_emi(principal, annual_rate, years)

        # Calculate total repayment and interest
        months = years * 12
        total_payment = emi * months
        total_interest = total_payment - principal

        # Display results
        print(f"\nCustomer: {name}")
        print("-" * 55)

        print(f"Loan Amount       : Rs. {principal:,.2f}")
        print(f"Annual Interest   : {annual_rate}%")
        print(f"Loan Tenure       : {years} years")
        print(f"Monthly EMI       : Rs. {emi:,.2f}")
        print(f"Total Repayment   : Rs. {total_payment:,.2f}")
        print(f"Total Interest    : Rs. {total_interest:,.2f}")

    except (ValueError, TypeError) as error:
        print(f"\nCustomer: {name}")
        print(f"Error: {error}")


# --------------------------------------------------
# STEP 4: INPUT VALIDATION TESTS
# --------------------------------------------------

print("\n" + "=" * 55)
print("             VALIDATION TESTS")
print("=" * 55)

test_cases = [
    ("Valid loan", 500000, 10, 5),
    ("Negative loan amount", -500000, 10, 5),
    ("Negative interest rate", 500000, -5, 5),
    ("Zero interest rate", 500000, 0, 5),
    ("Zero loan tenure", 500000, 10, 0),
    ("Invalid loan amount type", "500000", 10, 5)
]

for test_name, principal, rate, years in test_cases:

    try:
        result = calculate_emi(principal, rate, years)
        print(f"{test_name}: EMI = Rs. {result:,.2f}")

    except (ValueError, TypeError) as error:
        print(f"{test_name}: Correctly rejected - {error}")
