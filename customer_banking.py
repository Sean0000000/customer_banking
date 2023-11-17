# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import cd_account
create_cd_account = cd_account.create_cd_account
import savings_account
create_savings_account = savings_account.create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("Savings Account, Balance: ")
    savings_interest = input.float("Savings Account, Interest Rate Percentage: ")
    savings_maturity = input.int("Savings Account, Number of Months: ")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    interest = savings_balance * (savings_interest/100 * savings_maturity/12)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("CD, Balance: ")
    cd_interest = input.float("CD, Interest Rate Percentage: ")
    cd_maturity = input.int("CD, Number of Months: ")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    interest = cd_balance * (cd_interest/100 * cd_maturity/12)

if __name__ == "__main__":
    # Call the main function.