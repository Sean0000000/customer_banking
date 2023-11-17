"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
import Account
Account = Account.Account
import customer_banking

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_interest_rate = 0

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest = balance * (cd_interest/100 * months/12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    balance = interest + balance

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    balance_and_earned_interest = balance + cd_interest_rate

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    months = 12
    balance_and_earned_interest = cd_interest_rate / 12

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
balance_and_earned_interest = print("$"balance_and_earned_interest)