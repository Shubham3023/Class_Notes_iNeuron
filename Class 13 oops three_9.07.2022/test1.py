# multilevel Inheritance

class bank :

    def transection(self):
        print("Total transection value")

    def account_opening(self) :
        print("This will show you your account open status")

    def deposit(self):
        print("This will show your deposited amount")

class HDFC_bank(bank):

    def hdfc_to_icici(self):
        print("This will show you all the transection happened to icici through hdfc")

class icici(HDFC_bank):  # by default class HDFC_bank is available also Bank class
                        # is also available as HDFC_bank is child class of bank
    pass

i = icici()

i.hdfc_to_icici()
i.transection()
i.account_opening()
i.deposit()