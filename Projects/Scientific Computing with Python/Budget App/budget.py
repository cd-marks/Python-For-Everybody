class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.ledger_entries = list()
        self.ledger_output = list()
        self.amount = 0
    
    def deposit (self, dep_amount, description = ''):
        self.amount += dep_amount
        
        new_ledger_item = {"amount": self.amount, "description": description}
        self.ledger.append(new_ledger_item)

    def withdraw (self, with_amount, description = ''):
        amnt_check = self.check_funds(with_amount)
        if amnt_check == True:
            amount_check = True
            
            neg_with_amount = -with_amount
            self.amount -= with_amount
            
            new_ledger_item = {"amount": neg_with_amount, "description": description}
            self.ledger.append(new_ledger_item)
        else:
            amount_check = False

        return amount_check

    def get_balance (self):
        
        balance = self.amount
        
        return balance

    def transfer (self, transfer_amount, dest_category):
        amnt_check = self.check_funds(transfer_amount)
        if amnt_check == True:
            transfer_check = True

            with_description = 'Transfer to ' + dest_category.name
            self.withdraw(transfer_amount, with_description)

            dep_description = 'Transfer from ' + self.name
            dest_category.deposit(transfer_amount, dep_description)
        else:
            transfer_check = False

        return transfer_check

    def check_funds (self, check_amount):
        fund_check = self.amount < check_amount
        return not fund_check

    def __str__(self):
        line_length = 30
        border_length = int(((line_length-len(self.name))/2))
        title_line = (('*' * border_length) + self.name + ('*' * border_length))
        self.ledger_output.append(title_line)
        
        for entry in self.ledger:
            for k, v  in entry.items():
                self.ledger_entries.append(v)
                
        amount_index = 0
        desc_index = 1
        while amount_index < (len(self.ledger_entries) - 1) and desc_index < len(self.ledger_entries):           
            desc_value = str.ljust(self.ledger_entries[desc_index], int(line_length/2))
            desc_value = desc_value[:23]
            desc_length = len(desc_value)
            
            formatted_amount_value = "{:.2f}".format(self.ledger_entries[amount_index])
            amount_value = str.rjust(str(formatted_amount_value), int(line_length - desc_length))
            
            line_value = desc_value + amount_value
            self.ledger_output.append(line_value)
            amount_index = amount_index + 2
            desc_index = desc_index + 2

        total = str(self.get_balance())
        total_line = 'Total: ' +  total
        self.ledger_output.append(total_line)

        complete_output = ('\n').join(self.ledger_output)

        return complete_output
