class Labratories():
  #Adds and writes the lab name to the file in the format of the data that is in the file
  def addLabToFile(self): 
    f = open("files/laboratories.txt", "a")
    f.write("\n" + lab_change + "")
    f.close()

  #Writes the list of labs into the file laboratories.txt
  def writeListOfLabsToFile(self):
    with open("files/laboratories.txt", "w") as f:
      f.write("Lab\t\tCost\n\nLab1\t\t800\n\nLab2\t\t1200\n\nLab3\t\t500\n\nLab4\t\t50")
      f.close


  #Displays the list of laboratories
  def displayLabsList(self):
    loop = True # The final project will have loop set to global for this it needs to be loop = true
    while loop == True:
      print("Laboratories Menu:\n 1 - Display laboratories list\n 2 - Add laboratory\n 3 - Back to the Main Menu")
      user_input = int(input())
      if user_input == 1:
        self.readLaboratoriesFile(self)
      elif user_input == 2:
        self.enterLaboratoryInfo(self)
      elif user_input == 3:
        self.writeListOfLabsToFile(self)
        break
      else:
        print("Enter proper value")

  #Formats the Laboratory object similar to the laboratories.txt file
  def formatLabInfo(self):
    global lab_change
    lab_change = (lab + "\t\t" + cost)
    self.addLabToFile(self)

  #enterLaboratoryInfo	Asks the user to enter lab name and cost and forms a Laboratory object
  def enterLaboratoryInfo(self):
    global lab, cost 
    lab = input(print("\nEnter Lab name:\n"))
    cost = input(print("\nEnter Lab cost:\n"))
    self.formatLabInfo(self)

  #Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
  def readLaboratoriesFile(self):
    f =  open("files/laboratories.txt", "r")
    for line in f:
      print(line)
    f.close()

LAB = Labratories

LAB.displayLabsList(self=LAB)

''' print("Displays the list of laboratories")
    f = open("files/laboratories.txt", "r")
    f2 = f.read()
    f2a = f2.split("\n")
    line_lenght = len(f2a)
    for x in range(line_lenght):
      line = f2a[x].split("_")
      print("{:<10}{:<10}".format(line[0],line[1]))
    f.close()
    return
  readLaboratoriesFile()'''



  