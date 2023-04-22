class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function increments account balance
        :param amount: specified amount
        :return: Either true or false whether deposit is (un)/successful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Function decreases account balance
        :param amount: specified amount
        :return: True or False whether deposit (un)/successful
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function will return the balance
        :return: balance of the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function gets/returns account name
        :return: account name
        """
        return self.__account_name


    
