# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is the balance of your savings account? \n"))
    savings_interest = float(input("What is the interest rate of your savings account? \n"))
    savings_maturity = float(input("How many months will you leave the money in your savings account? \n"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    #create_savings_account(savings_balance, savings_interest, savings_maturity)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"At the end of {savings_maturity} months, your total balance will be ${updated_savings_balance:.2f}, with a total of ${interest_earned:.2f} in interest earned.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is the balance of your CD? \n"))
    cd_interest = float(input("What is the interest rate of your CD? \n"))
    cd_maturity = float(input("How many months will you leave the money in your CD? \n"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, CD_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"At the end of {cd_maturity} months, your total balance will be ${updated_cd_balance:.2f}, with a total of ${CD_interest_earned:.2f} in interest earned.")

if __name__ == "__main__":
    main()
