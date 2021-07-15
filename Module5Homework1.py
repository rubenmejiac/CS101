# Module5Homework1: Functions

# Collect information from the user
hoursworked = int(input("Please enter your work hours: "))
hourlyrate = int(input("Please enter your hourly rate: "))
state = input("Please enter your state of resident: ")
maritalstatus = input("Please enter your marital status: ")

def calculatewages(hoursworked, hourlyrate):
   wages = hoursworked * hourlyrate
   return wages

def calculatefedtax(maritalstatus, wages):
    taxpercent=0
    if (maritalstatus == "Married"):
        taxpercent=0.2
    elif (maritalstatus == "Single"):
        taxpercent=0.25
    else :
        taxpercent=0.22
    fedtax = wages * taxpercent
    return fedtax

def calculatestatetax(wages, state):
    statepercent=0
    if (state == "CA") or (state == "NV") or (state == "SD") or (state == "WA") \
        or (state == "AZ"):
        statepercent=0.08
    elif (state == "TX") or (state == "IL") or (state == "MO") or (state == "OH") \
        or (state == "VA"):
        statepercent=0.07
    elif (state == "NM") or (state == "OR") or (state == "IN"):
        statepercent=0.06
    else :
        statepercent=0.05
    statetax = (wages * statepercent)
    return statetax

def calculatenet(wages, fedtax, statetax):
    netwages = (wages - fedtax - statetax)
    return netwages

Wag = calculatewages(hoursworked, hourlyrate)
Ftx = calculatefedtax(maritalstatus, Wag)
Stx = calculatestatetax(Wag, state)
Nwg = calculatenet(Wag, Ftx, Stx)

print ("**********")
print("Your wage is: $" + str(Wag))
print("Your federal tax is: $" + str(Ftx))
print("Your state tax is: $"+str(Stx))
print("Your net wage is: $"+str(Nwg))
print ("**********")
