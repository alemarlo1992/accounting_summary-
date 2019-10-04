
# To Do
# Read through accounting.py and understand what it’s doing.
# Create a function that takes in a text file of customer orders and parses it to produce similar output.
# Add comments explaining what your code is doing.
# Read over the solution and see how it compairs to your answer.


def underpaid_melons(path):
#Create a fucntion that takes the file as an argument 

  melon_cost = 1.00
#represent the price of the melon

  file = open(path)
#set variable to open the file 

  for line in file: 
# create a for loop to iterate through each line 

    line = line.rstrip()
#delete any empty spaces 

    line = line.split('|')
#Create a list so we can access desired info through indices 

    customer_name = line[1]
    customer_melons = float(line[2])
    customer_paid = float(line[3])
#access the index that we want for our statement
#add float to eliminate the string 

    customer_expected = customer_melons * melon_cost
  #create equation for the amount of money that is expected from each customer 

    print("{} paid ${},expected ${}".format(customer_name, customer_paid, customer_expected))
#print that number 

    if customer_expected < customer_paid: 
      print("{} has underpaid".format(customer_name))

    elif customer_expected > customer_paid:
      print("{} has overpaid".format(customer_name))
  #create an if and elif to know who underpaid or overpaid for melons 
  file.close()

#close file 

underpaid_melons('customer-orders.txt')

#call fucntion so that our fuction is able to run 