#Get user names
userNameLast = input("What is your last name: ")
userNameFirst = input("What is your first name: ")
#Get hourly rate and working hours, then calculate wage
hourlyWage = input("What is your hourly wage: ")
workingHours = input("How many hours have you worked: ")
wage = int(hourlyWage) * int(workingHours)
#Output results
print("Your first name is " + userNameFirst)
print("Your last name is "+userNameLast)
print("Your wage is $" + str(wage))