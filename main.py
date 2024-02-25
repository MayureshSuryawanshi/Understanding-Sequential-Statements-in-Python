# input statements
salary = 0
numDependents = 0
stateTax = 0
federalTax = 0
dependentDeduction = 0
totalWithholding = 0
takeHomePay = 0


salary = float(input("Enter your salary amount:"))
numDependents = float(input("Enter your number of dependents:"))

# calculate taxes here
stateTax = salary * .065
print("State Tax: $" + str(stateTax))


federalTax = salary * .28
print("Fedral Tax: $" + str(federalTax))

dependentDeduction = (salary * .025) * numDependents
print("Dependents: $" + str(dependentDeduction))

totalWithholding = stateTax + federalTax + dependentDeduction

takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))