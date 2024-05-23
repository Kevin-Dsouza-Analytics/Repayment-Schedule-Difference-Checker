import numpy as np 
import pandas as pd 

def monthly_to_annual_IR(interest_rate):
    """
    Convert monthly interest rate to annual interest rate.

    Args:
    interest_rate (float): Monthly interest rate expressed as a decimal (e.g., 0.1 for 10%).

    Returns:
    float: Annual interest rate expressed as a decimal.
    """
    annual_IR = interest_rate * 12
    return round(annual_IR,6)

def annual_to_monthly_IR(interest_rate):
    """
    Convert annual interest rate to monthly interest rate.

    Args:
    interest_rate (float): Annual interest rate expressed as a decimal (e.g., 0.1 for 10%).

    Returns:
    float: Monthly interest rate expressed as a decimal.
    """
    monthly_IR = interest_rate / 12
    return round(monthly_IR,6)

    
def calculate_emi_amount(principal, interest_rate, loan_tenure):
  """
  Calculates the EMI (Equated Monthly Installment) for a loan.

  Args:
      principal: The principal loan amount (float).
      interest_rate: The annual interest rate (float).
      loan_tenure: The loan tenure in months (int).

  Returns:
      The EMI amount (float).
  """
  # Convert annual interest rate to monthly interest rate
  monthly_interest_rate = annual_to_monthly_IR(interest_rate)
  # Calculate the EMI
  emi = (principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** loan_tenure)) / (((1 + monthly_interest_rate) ** loan_tenure) - 1)
  return emi
    

def calculate_closing_balance(opening_balance, principal_amount):
    return round(opening_balance - principal_amount, 2)    


def get_percentage_format(number, decimal = 2):
        # Ensure the number is not zero to avoid division by zero
    if number == 0:
        return "Error: The number should not be zero."
    # Calculate the percentage
    percentage = number * 100
    percentage_rounded = "{:.2f}%".format(percentage)
    return percentage_rounded
    
def indian_accounting_format(number):
    """
    Formats a number into Indian Accounting Standard (Ind-AS) format with a rupee sign.
    
    Args:
        number: The number to format (float).
    
    Returns:
        A string representing the number in Ind-AS format with a rupee sign.
    """
    if number < 0:
        sign = ""
        number = abs(number)
    else:
        sign = ""
    
    # Splitting the integer and decimal parts
    integer_part = int(number)
    decimal_part = round(number - integer_part, 2)
    
    # Creating the decimal string
    decimal_str = f"{decimal_part:.2f}".split('.')[1]
    
    # Converting integer part to string for manipulation
    int_str = str(integer_part)
    
    # Formatting the integer part in Indian numbering system
    if len(int_str) > 3:
        int_str = int_str[-3:]  # last three digits
        rest = str(integer_part)[:-3]  # remaining digits
        
        while len(rest) > 2:
            int_str = rest[-2:] + ',' + int_str
            rest = rest[:-2]
        
        if rest:
            int_str = rest + ',' + int_str
    
    # Combine sign, rupee symbol, integer part and decimal part
    formatted_number = f"{sign}\u20B9 {int_str}.{decimal_str}"
    
    return formatted_number
