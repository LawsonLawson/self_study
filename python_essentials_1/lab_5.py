'''
Scenario
Once upon a time there was a land - a land of milk and honey, inhabited by
happy and prosperous people. The people paid taxes, of course - their happiness
had limits. The most important tax, called the Personal Income Tax
(PIT for short) had to be paid once a year, and was evaluated using the
following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal
to 18% of the income minus 556 thalers and 2 cents
(this was the so-called tax relief) if the income was higher than this amount,
the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over
85,528 thalers. Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a
function named round() which will do the rounding for you - you'll find it in
the skeleton code in the editor. Note: this happy country never returns money
to its citizens. If the calculated tax is less than zero, it only means no tax
at all (the tax is equal to zero). Take this into consideration during your
calculations.

Look at the code in the editor - it only reads one input value and outputs
a result, so you need to complete it with some smart calculations.

Test your code using the data we've provided.

Test Data
Sample input: 10000

Expected output: The tax is: 1244.0 thalers

Sample input: 100000

Expected output: The tax is: 19470.0 thalers

Sample input: 1000

Expected output: The tax is: 0.0 thalers

Sample input: -100

Expected output: The tax is: 0.0 thalers
'''
# first, we establish the 1 cent : 0.00147738 thalers
# hence make 2 cents : 0.00295476

# Tax limit to determine how much tax will be paid
tax_limit_amount = 85528.00

# Tax relief amount
tax_relief = 556.00295476

# Fixed tax for incomes over the limit amount
fixed_tax = 14839.00295476

# we collect the user income
try:
    # cast it into a float
    user_income = float(input("What is your income in thalers?: "))

    # checks if the user qualifies for a tax relief then computes tax
    if user_income < tax_limit_amount:
        tax_amount = ((18 / 100) * user_income) - tax_relief
        tax_amount = round(tax_amount, 0)

        # in case tax calcuated is less than 0, we assume the tax is 0
        if tax_amount <= 0:
            tax_amount = 0
        print("The tax is: {}".format(tax_amount))
    else:
        # checks wether user earns more than the limit amount
        if user_income > tax_limit_amount:

            # if yes, computes the excess
            excess = user_income - tax_limit_amount

            # now we calculate the 32% rate for the excess income + fixed tax
            tax_amount = fixed_tax + ((32 / 100) * excess)
        elif user_income == tax_limit_amount:
            tax_amount = fixed_tax
        tax_amount = round(tax_amount, 0)
        print("The tax is: {}".format(tax_amount))
except ValueError:
    print("Please Enter a valid income amount")
