
def calculate_emi(principal, annual_rate, years):

    # STEP 1: Validate loan inputs

    if principal <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    if years <= 0:
        raise ValueError("Loan tenure must be greater than zero.")

    # STEP 2: Convert annual rate into monthly rate
    monthly_rate = annual_rate / (12 * 100)

    # STEP 3: Convert years into months
    months = years * 12

    # STEP 4: Handle zero-interest loans
    if monthly_rate == 0:
        return principal / months

    # STEP 5: Calculate EMI
    emi = (
        principal * monthly_rate *
        (1 + monthly_rate) ** months
    ) / (
        (1 + monthly_rate) ** months - 1
    )

    return emi
