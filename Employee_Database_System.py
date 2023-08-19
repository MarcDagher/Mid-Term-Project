#C:\\Users\Dagher\Desktop\employee file

def InputPath(): # Time Complexity is O(n) => the code depends on the user's file input

  ## STEP 1: Receive input file and OPEN
  path = input("Insert Employee File location: ") # determine the file's path
  file_path = path + ".txt" # add the file's extention to complete path

  file = open(file_path, "r") 

  ## STEP 2: Store file's info in dictionary
  list_of_data = [] # list of nested lists storing distributed info of each employee. [empID,name,time,gender,salary]

  for i in file:
      new_line_1 = i.strip("\n") # line with no \n
      new_line_2 = new_line_1.split(", ") # remove commas and turn string into a list
      list_of_data.append(new_line_2) # store each line

  dictionary_of_employees = {}

  for i in list_of_data: # assigning each key to its dictionary of values
      id = i[0]
      name = i[1]
      date = i[2]
      gender = i[3]
      salary = i[4]
      dictionary_of_employees[id] = {"name" : name, "date" : date, "gender" : gender, "salary" : salary}
  print("File saved.")
  print()
  print("Enter Username and Password")
  return dictionary_of_employees

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# STEP 3: GREET USER and TAKE USERNAME + PASSWORD

def GreetUser(dict_of_employees): # Worst case answering wrong 5 times. Time Complexity O(n) where n is the input username and pass
    list_of_names = [] # store names

    for i in dict_of_employees:
        list_of_names.append(dict_of_employees[i]["name"])

    username = input("Username: ")
    count = 1
    
    while username != "admin" and username not in list_of_names and count < 5: # user errors (not found, more than 5 tries) note: admin isnt part of the file so we used and not or
        count += 1
        print("User not found!")
        username = input("Username: ")

    if count == 5:
        print("Too many tries...")
        print("Try again.")
        print()
        return GreetUser(dict_of_employees)


    password = input("Password: ") # ask for password
    if username == "admin": # if admin
        count = 1
        while password != "admin123123" and count < 5: #if worng password and exceeded limit
            print("wrong password")
            count += 1
            password = input("Password: ")
        if count == 5: 
            print("Too many tries.")
            print("Try again.")
            print()
            return GreetUser(dict_of_employees)
        if password == "admin123123":
            return AdminMenu(dict_of_employees)############# RETURN ADMIN'S MENU ############
        
    elif username in list_of_names: # if user
        count = 1
        while password != "" and count < 5:
            print("Wrong password!")
            count += 1
            password = input("Password: ")
        if count == 5:
            print("Too many tries.")
            print("Try again.")
            print()
            return GreetUser(dict_of_employees)
        if password == "":
            print("Hi,", username) ############## RETURN USER'S MENU ##############
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def AdminMenu(dict_of_employees): # O(n) where n is the user's input to more_actions

    def More_Actions(dict_of_employees): # O(n) where n is the number of times it takes the user to answer correctly
        more_actions = input("Would you like to do anything else? ")
        while more_actions != "Yes" and more_actions != "yes" and more_actions != "No" and more_actions != "no":
            print()
            print("Wrong entry! Answer yes or no.")
            more_actions = input("Would you like to do anything else? ")
        
        if more_actions == "Yes" or more_actions == "yes":
            print()
            return AdminMenu(dict_of_employees)
        elif more_actions == "No" or more_actions == "no":
            print()
            print("Goodbye :)")

    def Display_Stats(dict_of_employees): # O(1) since user doesn't have any inputs in this funcction so its a constant. Worst case is if the dictionary is super long.
        males = 0
        females = 0
        total = len(dict_of_employees)
        for i in dict_of_employees:
            if dict_of_employees[i]["gender"] == "male" or dict_of_employees[i]["gender"] == "Male":
                males += 1
            elif dict_of_employees[i]["gender"] == "female" or dict_of_employees[i]["gender"] == "Female":
                females += 1
        perc_of_males = (males/total)*100
        perc_of_females = (females/total)*100
        print("In the list of employees provided, {} are males and {} are females.".format(males, females))
        print("Your company is currently", perc_of_males, "% males and", perc_of_females,"%", "females")
        return More_Actions(dict_of_employees)

    # print(dict_of_employees)
    # print(list_of_names)
    print("Welcome Admin!")  # display menu items
    print()
    print("""
        1. Display Stats
        2. Add Employee
        3. Display Employees
        4. Change Employee Salary
        5. Remove Employee
        6. Raise Salary
        7. Exit""")
    print()
    action = input("What would you like to do? ") # user input command
    while action.isdigit() == False or int(action) not in range(1, 8) : # if choice is not a digit or not in the menu
        if action.isdigit() == False:
            print("Please choose a number between 1 and 7.")
            print()
            action = input("What would you like to do? ")
        elif int(action) not in range(1, 8):
            print("Make sure the number chosen is in the menu list!")
            print()
            action = input("What would you like to do? ")
    
    if action == "1":
        return Display_Stats(dict_of_employees)


dict_of_employees = InputPath()
GreetUser(dict_of_employees)