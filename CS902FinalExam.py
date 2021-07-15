# Initialize arrays
Names = []
ID = []
Score1 = []
Score2 = []
Score3 = []

# This function displays the menu, collects user response and sends it back

def displaymenu():
    print ("**** MENU OPTIONS ****")
    print ('Type P to populate the student information.')
    print ('Type U to update student Information')
    print ('Type D to display the student information.')
    print('Type C to calculate the Grade.')
    print('Type E to exit')
    print ("Please enter your choice: ")
    
    choice = input()
    return choice

def populateStudentInfo():
    position=0
    # This loops collects student information.
    while (position < 4):
        
        name = input("Please enter a student's name : ")
        Names.append(name)
        id = int(input("Please enter the student's ID: "))
        ID.append(id)
        sc1 = int(input("Please enter first score: "))
        Score1.append(sc1)
        sc2 = int(input("Please enter scond score: "))
        Score2.append(sc2)
        sc3 = int(input("Please enter third score: "))
        Score3.append(sc3)
        position = position + 1
    return

def searchForStudentId():
    #This function looks for student ID and displays student data
    idSearch = int(input('Please enter the ID of the student: '))
    foundposition = -1
    position = 0
    while (position < 4):
        if (idSearch == ID[position]):
                foundposition = position
                break
        position = position + 1
    if foundposition == -1:
        print("The ID is not found!")
        return
    nameSearch = Names[foundposition]
    nid = ID[foundposition]
    sc1 = Score1[foundposition]
    sc2 = Score2[foundposition]
    sc3 = Score3[foundposition]
    print ('The student name is: '+ nameSearch)
    print ('ID is: ' + str(nid))
    print ('First score  is: ' + str(sc1))
    print ('Second score  is:' + str(sc2))
    print ('Third score  is: ' + str(sc3))
    return

def updateStudentInfo():
    #This function looks for the student id, displays student data and updates student information
    idSearch = int(input('Please enter the ID of the student: '))
    foundposition = -1
    position = 0
    while (position < 4):
        if (idSearch == ID[position]):
                foundposition = position
                break
        position = position + 1
    if foundposition == -1:
        print("The ID is not found!")
        return
    nameSearch = Names[foundposition]
    nid = ID[foundposition]
    sc1 = Score1[foundposition]
    sc2 = Score2[foundposition]
    sc3 = Score3[foundposition]
    print ('The student name is: '+ nameSearch)
    print ('ID is: ' + str(nid))
    print ('First score is: ' + str(sc1))
    print ('Second score is:' + str(sc2))
    print ('Third score is: ' + str(sc3))
    
    pos = ID.index(idSearch)
    sc11 = int(input("Please enter first score: "))
    sc22 = int(input("Please enter scond score: "))
    sc33 = int(input("Please enter third score: "))
    Score1[pos] = sc11
    Score2[pos] = sc22
    Score3[pos] = sc33
    return

def calculateGrade():
    #This function calculates the grade based on the average of scores
    idSearch = int(input('Please enter the ID of the student: '))
    foundposition = -1
    position = 0
    while (position < 4):
        if (idSearch == ID[position]):
                foundposition = position
                break
        position = position + 1
    if foundposition == -1:
        print("The ID is not found!")
        return
    sc1 = Score1[foundposition]
    sc2 = Score2[foundposition]
    sc3 = Score3[foundposition]

    ave = (sc1 + sc2 + sc3)/3
    print ('The average is: '+ str(ave))
    if ave >= 90 and ave <=100:
        grade = 'A'
    elif ave >= 80 and ave <=89:
        grade = 'B'
    elif ave >= 70 and ave <=79:
        grade = 'C'
    elif ave >= 60 and ave <=69:
        grade = 'D'
    elif ave < 60:
        grade = 'F'
    print ("The grade is: " + grade)
    return

#Main begins here

response=''
while response != 'E' and response !='e':
       response = displaymenu()
       if response=='P' or response=='p':
              populateStudentInfo()
       elif response=='D' or response=='d':
              searchForStudentId()
       elif response=='U' or response=='u':
              updateStudentInfo()
       elif response=='C' or response=='c':
              calculateGrade()
       elif response=='E' or response=='e':
              print ('Thank you for using the program.')
              print ('Bye')
       else:
              print ('Invalid choice. Try again')
