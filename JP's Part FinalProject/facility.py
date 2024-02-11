class Facility():
  def addFacility(self):
    fcl_change = input("\nAdd Facility:\n")
    f = open("files/facilities.txt", "a")
    f.write( "\n" + fcl_change + "")
    f.close()
    return  

  def displayFacilities(self):
    loop = True # The final project will have loop set to global for this it needs to bee loop = true
    while loop == True:
      print("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n")
      fcl_change = int(input())
      if fcl_change == 0:
        break
      if fcl_change == 1:
        f = open("files/facilities.txt", "r")
        for line in f:
          print(line)
        f.close()
      elif fcl_change == 2:
        self.addFacility(self)
      elif fcl_change == 3:
        self.writeListOffacilitiesToFile()
        break
      else:
        print("Enter Proper value")
    return

  def writeListOffacilitiesToFile(self):
    f = open("files/facilities.txt", "w")
    f.write('''
      Hospital  Facility are:
      Ambulance
      Admit Facility 
      Canteen
      Emergency
      ''')
    f.close()
    return


FCL = Facility

FCL.displayFacilities(self=FCL)

