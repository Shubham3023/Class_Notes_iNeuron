# multiple inheritance

class bank:

    def __init__(self, working_hr):
        self.working_hr = working_hr

    def transactions_day(self):
        return "transections per day in bank is : {} ".format(15*self.working_hr)

    def total_cashflow(self, avg_trn_amt):
        return "total cash flow per day in bank is: {}".format(15*avg_trn_amt)

    def test(self):
        return "i am test method from bank class"


class hdfc_bank :

    def hdfc_to_ineuron(self):
        return "transactions from hdfc to ineuron bank is: {}".format(10*self.working_hr)

    def test(self):
        return "i am test method from hdfc_bank class"



class ineuron_bank:

    def ineuron_to_hdfc(self):
        return "transactions from ineuron to hdfc bank is: {}".format(5 * self.working_hr)

class icici(bank, hdfc_bank, ineuron_bank):

    def Vijay_malya(self):
        return "saab bank ka paisa leke UK Bhaag gaya"


i = icici(6)

# methods and variables from bank class
print("from bank value of working hr variable: ",i.working_hr)
print("from bank: ",i.transactions_day())
print("from bank: ",i.total_cashflow(800))
print("from bank: ",i.test())

# methods from ineuron_bank

print("from ineuron: ",i.ineuron_to_hdfc())

# methods from hdfc_bank

print("from hdfc: ",i.hdfc_to_ineuron())
print("from hdfc",i.test())   #this is comming from bank class as while creating inheritance for icici, class bank is written first,
                               #as both bank class and hdfc_bank class have a method by same name test, hence there is conflict.
                               #always the conflicted method will be called from the class mentioned first while writing inheritance.
                               #in this case from bank class
                               #to get test method from hdfc_bank class define inheritance as below
                               
                               #class icici(hdfc_bank, bank, ineuron_bank):
                               #     pass
                               #i = icici(6)
                               #print(i.test())
                               #output: i am test method from hdfc_bank class



# methods from icici bank class
print("from icici: ",i.Vijay_malya())


