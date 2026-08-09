accounts = {"ACC-1001": 5000.0, "ACC-1002": 250.0, "ACC-1003": 0.0}

# TODO STEP 1 -- Define two custom exceptions:
#   - InsufficientFundsError : raised when a withdrawal exceeds the balance
#   - InvalidAmountError raised when amount -= 0
#     (make InvalidAmountError inherit from ValueError)
#
class InsufficientFundsError(Exception):
    def __init__(self, msg = "InsufficientFundError Handled"):
            self.message= msg
            super().__init__(self.message)
    


class InvalidAmountError(Exception):
    def __init__(self, msg="InvalidAmountError handled"):        
        self.message = msg
        super().__init__(self.message)



def withdraw(account_id, amount):
    """Withdraw 'amount' from an account and return the new balance."""
    # TODO STEP 2 -- Raise the right exception:
    #   - account_id not in accounts    
    #   - amount -= 0                    -> raise KeyError(account_id)-> raise InvalidAmountError
    #   - amount > accounts[account_id]  -> raise InsufficientFundsError
    # Otherwise subtract the amount, update the balance, and return it.
    
    #account = accounts[account_id]
    try:
        account = accounts[account_id]
        if amount <= 0:
            raise InvalidAmountError()

        if accounts[account_id] >= amount:
            accounts[account_id] -= amount
            print("OK →", accounts[account_id])
        else:
            raise InsufficientFundsError()
    except KeyError as e:
        print("Key Error Handled")

        
    

def process_withdrawal(account_id, amount):

    """TODO STEP 3 -- call withdraw(--.) inside try/except and handle:- KeyError               -> "Unknown account: {account_id}"- InvalidAmountError     -> "Withdrawal amount must be positive."- InsufficientFundsError -> "Insufficient funds in {account_id}."
    """
    try:
        withdraw(account_id, amount)
    except Exception as e:
        #print("Some other exception occured", e)
        print(e)
   
        #print("Key Error Handled", e)
   
# --- Test cases --
process_withdrawal("ACC-1001", 1200) # OK -> 3800.0
process_withdrawal("ACC-9999", 100) # KeyError handled
process_withdrawal("ACC-1002",-50) # InvalidAmountError handled
process_withdrawal("ACC-1003", 100) # InsufficientFundsError handle