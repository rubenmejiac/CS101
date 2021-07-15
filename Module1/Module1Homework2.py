#Get the price of three items and format them as numbers
price1 = float(input("Enter price of first Item:$ "))
price2 = float(input("Enter price of second item:$ "))
price3 = float(input("Enter price of third item:$ "))

#Calculate total
total = "{:,.2f}".format(price1 + price2 + price3)

#Display output
print ("Total price for all three items:$" + str(total))