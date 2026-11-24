# loan-emi-amortization-engine
Python-based loan EMI calculator with amortization and repayment scenario analysis
# Loan EMI & Amortization Engine with Scenario Analysis

## Project Overview

A Python-based FinTech project designed to calculate loan EMIs, total repayment amounts, and total interest using the reducing-balance method.

The project aims to demonstrate how financial mathematics can be translated into a practical lending application.

## Problem Statement

Borrowers often focus only on their monthly EMI without understanding the total interest payable over the loan tenure.

This project aims to build a tool that helps users understand loan repayment obligations and eventually compare different repayment strategies.

## Current Features

- Calculate monthly EMI using the reducing-balance formula.
- Convert annual interest rates into monthly interest rates.
- Convert loan tenure from years into monthly instalments.
- Handle zero-interest loan calculations.
- Calculate total repayment amount.
- Calculate total interest payable.
- Calculate EMI for multiple loan scenarios.

## Technology Stack

- Python
- Google Colab (development environment)
- GitHub (version control and documentation)

## Sample Test Cases

| Customer | Principal | Annual Rate | Tenure |
|---|---:|---:|---:|
| A | ₹5,00,000 | 10% | 5 years |
| B | ₹10,00,000 | 12% | 10 years |
| C | ₹20,00,000 | 8.5% | 15 years |

## Development Roadmap

### Phase 1: Core EMI Calculator
- [x] EMI calculation function
- [x] Monthly interest conversion
- [x] Tenure conversion
- [x] Zero-interest loan handling
- [x] Total repayment calculation
- [x] Total interest calculation

### Phase 2: Amortization Engine
- [ ] Monthly amortization schedule
- [ ] Principal and interest breakdown
- [ ] Outstanding loan balance

### Phase 3: Scenario Analysis
- [ ] Lump-sum prepayment
- [ ] Increased EMI scenario
- [ ] Fixed vs. floating interest rate comparison
- [ ] Interest savings analysis

### Phase 4: Application Development
- [ ] Pandas integration
- [ ] Financial visualizations
- [ ] Streamlit interface
- [ ] Unit testing
- [ ] Application deployment

## Learning Objectives

- Apply financial mathematics using Python.
- Understand loan amortization and reducing-balance calculations.
- Develop financial calculation functions.
- Build a practical FinTech application.
- Learn software testing and financial validation.

## Project Status

**Version 0.1 — Initial EMI Calculator**

This project is currently under development. Features will be added incrementally as the financial calculation engine evolves.
