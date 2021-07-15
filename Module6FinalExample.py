namelist=[]
hoursworkedlist=[]
hourlyratelist=[]
wagelist=[]

def populatelist():
       print ('I am inside the populate function')
       position=0
       #This loops collects five names and appends them to the namelist
       while(position< 3):
           name= input('Enter a name ')
           namelist.append(name)
           hours =int(  input('Enter hours worked ' ) )
           hoursworkedlist.append(hours)
           rate = int(  input('Enter hourly rate ') )
           hourlyratelist.append(rate)
           position = position + 1
       return


def displayall():
       print ('I am inside display function')
       pos =0
       #This loop, prints one name at a time from zeroth position to the end.
       while ( pos < 3):
              displayoneemployee(pos )
              pos = pos + 1
       return

def displayoneemployee(pos1):
       print (namelist[pos1],'hours worked ', hoursworkedlist[pos1], 'hourly rate ',hourlyratelist[pos1], ' wage is ', wagelist[pos1] )
       return

#This function is supposed to calculate the wage for each person.

def calculatewagelist():
       position=0
       while(position < 3):
              wage = hoursworkedlist[position] * hourlyratelist[position]
              wagelist.append( wage )
              position = position +1
       return

#What does it receive. Name to search
#what does it do? Searches for the name
#what does it send back. Position of the name, if not found, -1
def searchforname(nametosearch):
       foundposition=-1 # assume that it is not going to be found.
       position=0
       while (position < 3):
              if (nametosearch==namelist[position]):
                     foundposition = position
                     break
              position = position + 1

       return foundposition

#This function displays the menu, collects the user response and sends it back.
def displaymenu():
       print ('Enter P to populate data')
       print ('Enter C to calcualte wage')
       print ( 'Enter S to search for name ')
       print ('Enter U to update data')
       print ('Enter H to display employee with highest wage')
       print ('Enter E to exit')
       choice = input('Enter your choice')
       return choice

def updateoneemployeedata():
       #ask the user to enter employee name.
       #find the employee in namelist and gets its position.
       #take the new hourly rate and hours worked from the user.
       # update hourlyrate and hours worked, wage at THAT Position.
       nametoupdate = input("Enter employe name to udpate")
       foundpos = searchforname(nametoupdate)
       if (foundpos== -1 ):
              print ('Name not found')
       else:
              hourlyratelist[foundpos] =int(  input('Enter new hourly rate') )
              hoursworkedlist[foundpos] = int(  input('Enter new hours worked') )
              wagelist[foundpos] = hourlyratelist[foundpos] * hoursworkedlist[foundpos]

def findemployeewithhighestwage():
       highpos=0
       pos=1
       while (pos < 3):
              if wagelist[pos] > wagelist[highpos]:
                     highpos = pos
              pos = pos + 1

       return highpos

#main begins here
response=''
while response!= 'E' and response!='e':
       response = displaymenu()
       if response=='P' or response=='p':
              populatelist()
       elif response=='h' or response=='H':
              hpos = findemployeewithhighestwage()
              print (' person with highest wages is ' , namelist[hpos])
       elif response=='C' or response=='c':
              calculatewagelist()
       elif response=='U' or response=='u':
              updateoneemployeedata()
       elif response=='S' or response=='s':
              nametofind = input('Please enter the name to search')
              foundpos = searchforname(nametofind)
              if ( foundpos == -1 ):
                     print ('Name not found')
              else:
                     displayoneemployee(foundpos)
       elif response=='E' or response=='e':
              print ('Thank you for using the program')
              print ('Bye')
       else:
              print ('Invalid choice. Please try again')

 