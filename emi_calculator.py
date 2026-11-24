
import math


def validate_inputs(principal, annual_rate, years):
    """
    Validate the loan inputs before performing calculations.
    """

    inputs = {
        "Loan amount": principal,
        "Annual interest rate": annual_rate,
        "Loan tenure": years
    }

    for name, value in inputs.items():

        # Reject text, Boolean values and other invalid types
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number.")

        # Reject infinity and NaN
        if not math.isfinite(value):
            raise ValueError(f"{name} must be a finite number.")

    if principal <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    if years <= 0:
        raise ValueError("Loan tenure must be greater than zero.")

    # Loan tenure must convert into a whole number of monthly instalments
    months = years * 12

    if not months.is_integer():
        raise ValueError(
            "Loan tenure must result in a whole number of months."
        )


def calculate_emi(principal, annual_rate, years):
    """
    Calculate monthly EMI using the reducing-balance method.

    Parameters:
        principal: Loan amount
        annual_rate: Annual interest rate in percentage
        years: Loan tenure in years

    Returns:
        Monthly EMI
    """

    # STEP 1: Validate inputs
    validate_inputs(principal, annual_rate, years)

    # STEP 2: Convert annual interest rate into monthly decimal rate
    monthly_rate = annual_rate / (12 * 100)

    # STEP 3: Convert years into monthly instalments
    months = int(years * 12)

    # STEP 4: Handle zero-interest loans separately
    if monthly_rate == 0:
        return principal / months

    # STEP 5: Calculate EMI using the reducing-balance formula
    rate_factor = (1 + monthly_rate) ** months

    emi = (
        principal * monthly_rate * rate_factor
    ) / (
        rate_factor - 1
    )

    return emi


def calculate_loan_summary(principal, annual_rate, years):
    """
    Calculate EMI, total repayment and total interest.
    """

    # Calculate monthly EMI
    emi = calculate_emi(principal, annual_rate, years)

    # Calculate total number of instalments
    months = int(years * 12)

    # Calculate total repayment
    total_payment = emi * months

    # Calculate total interest
    total_interest = total_payment - principal

    return {
        "emi": emi,
        "total_payment": total_payment,
        "total_interest": total_interest,
        "months": months
    }


def display_loan_summary(customer):
    """
    Display loan details for an individual customer.
    """

    principal = customer["principal"]
    annual_rate = customer["rate"]
    years = customer["years"]

    result = calculate_loan_summary(
        principal,
        annual_rate,
        years
    )

    print("\n" + "=" * 40)
    print(f"Loan Summary: {customer['name']}")
    print("=" * 40)

    print(f"Loan Amount:       ₹{principal:,.2f}")
    print(f"Annual Rate:       {annual_rate}%")
    print(f"Loan Tenure:       {years} years")
    print(f"Number of EMIs:    {result['months']}")

    print("-" * 40)

    print(f"Monthly EMI:       ₹{result['emi']:,.2f}")
    print(f"Total Repayment:   ₹{result['total_payment']:,.2f}")
    print(f"Total Interest:    ₹{result['total_interest']:,.2f}")

    print("=" * 40)


def main():

    # Sample customer loan data
    customers = [
        {
            "name": "Customer A",
            "principal": 500000,
            "rate": 10,
            "years": 5
        },
        {
            "name": "Customer B",
            "principal": 1000000,
            "rate": 12,
            "years": 10
        },
        {
            "name": "Customer C",
            "principal": 2000000,
            "rate": 8.5,
            "years": 15
        }
    ]

    # Calculate and display each customer's loan summary
    for customer in customers:
        try:
            display_loan_summary(customer)

        except (ValueError, TypeError) as error:
            print(f"\nError for {customer['name']}: {error}")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
