namelist=[]
accountnumberlist=[]
balancelist=[]

def populatelist():
       position=0
       #This loops collects five names and appends them to the namelist
       while(position < 5):
           name= input('Please enter a name: ')
           namelist.append(name)
           hours =int(input('Please enter an account number: '))
           accountnumberlist.append(hours)
           rate = int(input('Please enter a balance '))
           balancelist.append(rate)
           position = position + 1
       return

def displayall():
       pos =0
       #This loop, prints one name at a time from zeroth position to the end.
       while (pos < 5):
              displayperson(pos)
              pos = pos + 1
       return

def displayperson(pos1):
       #print (namelist[pos1],'hours worked ', hoursworkedlist[pos1], 'hourly rate ',hourlyratelist[pos1], ' wage is ', wagelist[pos1] )
       return


'''
def calculatewagelist():
       position=0
       while(position < 3):
              wage = hoursworkedlist[position] * hourlyratelist[position]
              wagelist.append( wage )
              position = position +1
       return
'''
def searchforname(nametosearch):
       foundposition = -1 # assume that's not going to be found
       position=0
       while (position < 3):
              if (nametosearch==namelist[position]):
                     foundposition = position
                     break
              position = position + 1

       return foundposition

#This function displays the menu, collects user response and sends it back
def displaymenu():
       print ("**** MENU OPTIONS ****")
       print ('Type P to populate accounts')
       print ('Type S to search for account')
       print ('Type D to deposit Amount')
       print('Type W to withdraw Amount')
       print('Type E to exit')
       choice = input()
       return choice

'''
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
              hourlyratelist[foundpos] =int(input('...'))
              hoursworkedlist[foundpos] = int(input('...'))
              wagelist[foundpos] = hourlyratelist[foundpos] * hoursworkedlist[foundpos]
'''
def deposit():
       pos=0
       accttodeposit = int(input('Please enter the account number to add deposit:'))
       pos == accttodeposit
       return pos

#main begins here
response=''
while response!= 'E' and response!='e':
       response = displaymenu()
       if response=='P' or response=='p':
              populatelist()
       elif response=='W' or response=='w':
              #calculatewagelist()
              print ('...')
       elif response=='D' or response=='d':
              deposit()
       elif response=='S' or response=='s':
              nametofind = input('Please enter the name to search')
              foundpos = searchforname(nametofind)
              if ( foundpos == -1 ):
                     print ('Name not found')
              else:
                     displayperson(foundpos)
       elif response=='E' or response=='e':
              print ('Thank you for using the program')
              print ('Bye')
       else:
              print ('Invalid choice. Please try again')

 