monthName=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']

milesDriven=[]

#This function displays the menu, collects user response and sends it back

def displaymenu():

    print ("**** MENU OPTIONS ****")

    print ('Type P to populate miles and month name.')

    print ('Type S to search for Month')

    print ('Type M to search for Month name with smallest Miles')

    print('Type L to search for Month Name with Largest Miles')

    print('Type E to exit')

    choice = input()

    return choice

 

def populateMilesDriven():

       position=0

       #This loops collects 12 month names and miles driven for each month.

       while(position < 12):

           month = monthName[position]

           miles= input('Please enter miles driven for ' + month +': ')

           milesDriven.append(miles)

           position = position + 1

       return

 

def searchForMonth():

    #This function looks for the driven miles for an specific month

       monthSearch= input('Please enter the month name to search: ')

       if monthSearch in monthName:

            pos = monthName.index(monthSearch.upper())

            milesSearch = milesDriven[pos]

            print ('The month name is: '+ monthSearch + ' and the miles driven for the month is: '+ milesSearch )

       else:

           print('The month name not found!')
       
       return


def searchForSmallest():

    #This function looks for the month with the smallest miles

       smallestMiles = min(milesDriven)

       pos = milesDriven.index(smallestMiles)

       month = monthName[pos]

       print('The result for searching the smallest miles:')

       print ('The month name is: '+ month + ' and the miles driven for the month is: '+ smallestMiles )

       return

 

def searchForLargest():

    #This function looks for the month with the largest miles

       largestMiles = max(milesDriven)

       pos = milesDriven.index(largestMiles)

       month = monthName[pos]

       print('The result for searching the largest miles:')

       print ('The month name is: '+ month + ' and the miles driven for the month is: '+ largestMiles )

       return 

#main begins here

response=''

while response!= 'E' and response!='e':

       response = displaymenu()

       if response=='P' or response=='p':

              populateMilesDriven()

       elif response=='S' or response=='s':

              searchForMonth()

       elif response=='M' or response=='m':

              searchForSmallest()

       elif response=='L' or response=='l':

              searchForLargest()

       elif response=='E' or response=='e':

              print ('Thank you for using the program')

              print ('Bye')

       else:

              print ('Invalid choice. Please try again')