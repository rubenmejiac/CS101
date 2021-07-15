Names = []
AccountNumbers = []
Balance = []

# Populate the arrays
def populatearray():

   for position in range(5):
       name = input("Please enter a name ")
       Names.append(name)
       acctnum= int(input("Please enter an account number: "))
       AccountNumbers.append(acctnum)
       bal= int(input("Please enter a balance: "))
       Balance.append(bal)
       return

# Display contents of the arrays
def displayarray(numb, name, bal):

    for position in range(5):
          print("Name is ", Names[position])
          print (name + " account has the balance of : $"+str(bal))
          return

# Main
Choice = input ("Type P to populate accounts\
\
                Type S to search for account.\
\
                Type E to exit.")

if Choice == ("P"):
    # call populatearray() function to populate the array
    populatearray()

elif Choice ==("S"):
    numb = input ("Please enter the account number to search: ")
    displayarray(numb, name, bal)
    
elif Choice == ("E"):
    print("Thank you for using the program")
    print ("Bye")
