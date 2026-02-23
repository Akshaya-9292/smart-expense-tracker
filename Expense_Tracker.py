class expensetracker:
    def __init__(self):
        self.filename="EXPENSE_TRACKER.txt"
    def Amount(self):
        amount=float(input("Enter amount: "))
        category=input("Enter Category: ")
        with open(self.filename,"a") as aa:
            aa.write(f"{amount},{category}\n")
            print("Added Successfully")
    def add_expense(self):
        total = 0
        with open(self.filename, "r") as bb:
            for line in bb:
                amount = float(line.split(",")[0])
                total += amount
        print("Total Expense =", total)

a=expensetracker()
a.Amount()
a.add_expense()



# total=0
# expense=[]
# with open("EXPENSE_TRACKER.txt", "r") as f:
#    for line in f:
#     category,expense = line.strip().split(",")
#     total += float(expense)
#     expense.append((expense))
