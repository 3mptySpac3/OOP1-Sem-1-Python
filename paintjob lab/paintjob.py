print("Welcome to Shiny Paint company for indoor painting!")
def computePaintPrice(totalArea):
    return computeGallons(totalArea)*42 

def computeGallons(totalArea):
    return round((totalArea/350),2)

def computeRectangleWallsArea(): 
  print("\nEnter the length of the room in feet:\n")
  length=int(input())
  print("\nEnter the widht of the room in feet:\n")
  width=int(input())
  print("\nEnter the height of the room in feet:\n")
  height=int(input())
  return  float(2 * CRArea (length, width) + 2 * CRArea(width,height)- computeWindowsDoorsArea())

def CRArea(lenght, width):
  return lenght * width

def computeSquareWallsArea():
  print("\nEnter the length of one side of the room in feet:\n")
  lenght=int(input())
  return computeSquareArea(lenght) - computeWindowsDoorsArea()


def computeSquareArea(lenght):
  return 4 * (lenght * lenght)

def computeWindowsDoorsArea():
  print("\nHow many windows and doors does the room contain?\n")
  numberofdoorswindows= int(input())
  endValue=0
  for n in range(numberofdoorswindows):
    extraArea=int(input(f"\nEnter the length of window/door {n+1} in feet.\n"))
    print(f"\nEnter the width of window/door {n+1} in feet:\n")
    endValue += extraArea * int(input())
  return endValue

def computeCustomWallsArea():
  print("\nHow many walls in the room:\n")
  numberOfWalls=int(input())
  endValue=0
  for n in range(numberOfWalls):
    print(f"\nEnter the height of wall {n+1} in feet:\n")
    extraArea=int(input())
    print(f"\nEnter the length of wall {n+1} in feet:\n")
    endValue += extraArea * int(input())
  return endValue - computeWindowsDoorsArea()


def computeRoomArea(shape):
  totalArea=0
  for n in range(shape):
    print(f"Room {n+1}")
    print('''Select the shape of the room:
        1 – Rectangular
        2 – Square
        3 – Custom (more or less than four walls. All walls square or rectangular)''')
    number= int(input())
    if number == 1:
      finalArea= computeRectangleWallsArea()
      print(f"For Room: {n+1}, the area to be painted is {finalArea} square ft and will require {computeGallons(finalArea)} gallons of paint. This will cost the customer ${computePaintPrice(finalArea)}")
      totalArea += finalArea
    elif number == 2:
      finalArea= computeSquareWallsArea()
      print(f"For Room: {n+1}, the area to be painted is {finalArea} ft2 and will require {computeGallons(finalArea)} gallons of paint. This will cost the customer ${computePaintPrice(finalArea)}")
      totalArea += finalArea
    elif number == 3:
      finalArea= computeCustomWallsArea()
      print(f"For Room: {n+1}, the area to be painted is {finalArea} ft2 and will require {computeGallons(finalArea)} gallons of paint. This will cost the customer ${computePaintPrice(finalArea)}")
      totalArea += finalArea
    else:
      print("Wrong Input")
  print(f"\n\nArea to be painted is {totalArea} feet and will require {computeGallons(totalArea)} gallons of paint. This will cost the customer ${computePaintPrice(totalArea)}.\n")



print("\nWelcome to Shiny Painting for indoor painting!\n")
room=int(input("\nHow many rooms do you want to paint:\n"))
print("\nThank you!\n")
computeRoomArea(room)

