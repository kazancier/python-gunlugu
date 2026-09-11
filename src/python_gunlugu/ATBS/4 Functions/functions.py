def after_transaction(balance, transaction_amount):
    """
    This function calculates the new balance after a transaction.

    Parameters:
    balance (float): The current balance before the transaction.
    transaction_amount (float): The amount of the transaction. 
                                Positive for deposits, negative for withdrawals.

    Returns:
    float: The new balance after the transaction.
    """
    new_balance = balance + transaction_amount
    if new_balance < 0:
        return balance
    else:
        return new_balance

while True:
    try:
        current_balance = float(input("Enter your current balance: "))
        transaction = float(input("Enter the transaction amount (positive for deposit, negative for withdrawal): "))
        updated_balance = after_transaction(current_balance, transaction)
        print(f"Your new balance is: {updated_balance}")
    except ValueError:
        print("Please enter valid numerical values for balance and transaction amount.")