# This is a calculator to Create an application that automatically
#  calculates Circle Phones’ total profit for a one-day period.


appleiphone= 0
anddroidphone= 0
appletablet= 0
androidtablet= 0
windowstablet= 0

AppPhoneCost= 120.45
AndPhoneCost= 99.50
AppTabletCost= 75.69
AndTabletCost= 65.73
WindTabletCost= 51.49

print("Welcome to Circle Phones' Profit calculator.")
print()

for answer in range(5):
  answer = input("Enter product number 1-5, or enter 0 to stop: \n")
  
  if answer == "1":
    sold = int(input("Enter quantity sold: \n"))
    appleiphone = AppPhoneCost * sold 
  elif answer == "2":
    sold = int(input("Enter quantity sold: \n"))
    anddroidphone = AndPhoneCost * sold
  elif answer == "3":
    sold = int(input("Enter quantity sold: \n"))
    appletablet = AndTabletCost * sold
  elif answer == "4":
    sold = int(input("Enter quantity sold: \n"))
    androidtablet = AndTabletCost * sold
  elif answer == "5":
    sold = int(input("Enter quantity sold: \n"))
    windowstablet = WindTabletCost * sold
  elif answer == "0":
    break
  else:
    print("You blundered...")

everything = appleiphone + anddroidphone + appletablet + androidtablet + windowstablet
print("Your total profit for today is:", (everything))