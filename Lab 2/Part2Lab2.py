'''This is Circle Phone Calculator Part 2'''

wrongvalue=("Wrong value was entered!")#Error message variable
days = {
    8:"Monday",
    7:"Tuesday",
    6:"Wednesday",
    5:"Thursday",
    4:"Friday",
    3:"Saturday",
    2:"Sunday",
}

startV = False#ends or exits code from the begining
while startV == False:
    print("\nWelcome to circle Phones's profit Calculator!\n")
    print("You can calculate the profit of the company according to a specific day of by week or divide the week into weekdays and weekend")
    print()
    print("1 - For a specific day\n2 - For a whole week\n3 - For a work week (Monday-Friday)\n4 - For a weekend (Saturday–Sunday)\n0 - Exit")
    print()
    Enter=int(input())
    profit = [0, 0, 0, 0, 0]#total quantity profit per product(tqppp)
    weekproffit=[0, 0, 0, 0, 0, 0, 0, 0, 0]#holds value for weekly profit
    #dictionary below stores the keys of days
    count = 0#Counts
    reduction = 0
    choice = ''
    number = 1 #product number
    if Enter == 1:
        reduction = 2
        day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n")
        day = day.lower()
        day = day.capitalize()
    elif Enter == 2:
        reduction = 8
        choice = ("Week")
    elif Enter == 3:
        reduction = 6
        choice = ("Week(Buisness days)")
    elif Enter == 4:
        reduction = 3
        choice = ("Weekend")
    elif Enter == 0:
        startV = True
        count = 1
    else:
        wrongvalue

    while reduction >1:
        if Enter == 2:
            day = days[reduction]
            print("For", day)
        elif Enter == 3:
            day = days[reduction+2]
            print("For", day)
        elif Enter == 4:
            day = days[reduction+3]
            print("For", day)
        elif Enter == 1:
            print("For", day)
        elif startV == True:
            break

        while (count <= 5):
            number = float(input("Enter product number 1-5 or 0 to stop\n"))
            if number == 0:
                break
            #total quantity profit per product
            soldT = float(input("Enter quantity sold:\n"))
            if number == 1:
                endV = soldT*120.45
            elif number == 2:
                endV = soldT*99.50
            elif number == 3:
                endV = soldT*75.69
            elif number == 4:
                endV = soldT*65.73
            elif number == 5:
                endV = soldT*51.49
            count+=1
            profit[count] = endV
            #taking the value of the count to get the location in the list
        EndProfit = sum(profit)
        num = 1
        weekproffit[num] = EndProfit
        num+= 1
        reduction-=1 
    
    final = sum(weekproffit)

    if Enter == 1:
        print(f"Total Profit for the {day} is: ${round(final, 2)}")
        if final <10000:
            print("\nMore hard work needed... The last ", day ,"wasn't the best")
        else:
            print("\nYou did good this", day)
    elif Enter == 2 or Enter == 3 or Enter == 4:
        print(f"Total Profit for the {choice} is: ${round(final, 2)}")
        if final <10000:
            print("\nMore hard work needed... The last ", choice ,"wasn't the best")
        else:
            print("\nYou did good this", choice)
  


