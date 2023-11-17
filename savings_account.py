"""Imports the SavingsAccount class and attributes from the Account.py file."""
# ADD YOUR CODE HERE
import Account
Account = Account.Account
import customer_banking

# Define a function for the Savings Account
savings_interest = float(interest_rate)

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    interest = balance * (savings_interest/100 * months/12)
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    orignal_interest = 0

    # Calculate interest earned
     # ADD YOUR CODE HERE
    earned_interest = balance - (savings_interest/12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    balance_and_earned_interest = balance + earned_interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_interest = balance_and_earned_interest

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    months = 12
    balance_and_earned_interest = earned_interest / 12 months

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
balance_and_earned_interest = print("$"balance_and_earned_interest)
