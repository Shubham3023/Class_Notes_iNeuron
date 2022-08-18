# Multiple inheritance

class bank :

    def transection(self):
        print("Total transection value")
    def account_opening(self) :
        print("This will show you your account open status")
    def deposit(self):
        print("This will show your deposited amount")

    def test(self):
        print("this is a test method from bank class")

class HDFC_bank:

    def hdfc_to_icici(self):
        print("This will show you all the transection happened to icici through hdfc")

    def test(self):
        print("this is a test method from hdfc bank class")

class ineuron_bank :
    def account_status_icici(self):
        print("print a account status in icici bank")

class icici(HDFC_bank, bank, ineuron_bank) : # try class icici(bank, HDFC_bank)
    pass

i = icici()

i.transection()
i.account_opening()
i.deposit()
i.hdfc_to_icici()
i.test()   # due to method name test conflict, method will be available from first class mentioned in
            # inheritance class def i.e. see previous comment

i.account_status_icici()