
# To Do
# Read through accounting.py and understand what it’s doing.
# Create a function that takes in a text file of customer orders and parses it to produce similar output.
# Add comments explaining what your code is doing.
# Read over the solution and see how it compairs to your answer.


def underpaid_melons(path):

  melon_cost = 1.00

  file = open(path)

  for line in file: 

    line = line.rstrip()

    line = line.split('|')

    customer_name = line[1]
    customer_melons_str = line[2]
    customer_melons = int(customer_melons_str)
    customer_paid = line[3]

    customer_expected = customer_melons * melon_cost

    if customer_expected != customer_paid:

      print("{} paid ${},expected ${}".format(customer_name, customer_paid, 
            customer_expected)
            )

underpaid_melons('customer-orders.txt')