# Module5Homework2: Functions

# Collect information from the user
bus1pass = int(input("Please enter the number of passengers for bus1 :"))
bus2pass = int(input("Please enter the number of passengers for bus2 :"))
bus3pass = int(input("Please enter the number of passengers for bus3 :"))

def totalpass():
   passengers = bus1pass + bus2pass + bus3pass
   return passengers

def totalfare(passengers):
    fare = passengers * 2.5
    return fare

def netprofit(fare):
    operatingcosts = (fare * 0.5)
    net = fare - operatingcosts 
    return net

TotP = totalpass()
TotF = totalfare(TotP)
NetP = netprofit(TotF)

print ("***********")
print("There are total "+str(TotP)+" passengers from three buses.")
print("The total fare earned is: $"+ str(TotF))
print("The net profit is: $"+str(NetP))
print ("***********")
