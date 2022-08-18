# multileval inheritance

class bank:

    def __init__(self, working_hr):
        self.working_hr = working_hr

    def transactions_day(self):
        return "transections per day in bank is : {} ".format(15*self.working_hr)

    def total_cashflow(self, avg_trn_amt):
        return "total cash flow per day in bank is: {}".format(15*avg_trn_amt)


class hdfc_bank(bank):

    def hdfc_to_icici(self):
        return "transactions from hdfc to icici bank is: {}".format(10*self.working_hr)

class icici_bank(hdfc_bank):

    def icici_to_hdfc(self):
        return "transactions from icici to hdfc bank is: {}".format(5 * self.working_hr)

i = icici_bank(6)


# method from icici
print("from icici: ",i.icici_to_hdfc())

# method from hdfc
print("from hdfc: ",i.hdfc_to_icici())

# method from bank
print("from bank: ",i.transactions_day())
print("from bank: ",i.total_cashflow(900))


