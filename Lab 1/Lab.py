# This is a bill calculator, its function is to calculate your total monthly expenses 
# This calculator will add your gas and electric bill dependant on if
# you go over the set point of 1000kwh and 950GJ.
# Dependant on your province it will also tax you appropraitly.


print("Welcome to the Global Energy bill calculator!")

print(input("Enter the Account Number.""\n"))
'''
Constant_elec = 120.62
Efixed = 8.36
Efixedii = 9.41
Efloat = 9.11

Constant_gas = 1.32
Gfixed = 4.56
Gfloating = 3.93
'''
'''
months = {
    "1": "January",
    "01": "January",
    "2": "Febuary",
    "02": "Febuary",
    "3": "March",
    "03": "March",
    "4": "April",
    "04": "April",
    "5": "May",
    "05": "May",
    "6": "June",
    "06": "June",
    "07": "July",
    "7": "July",
    "8": "August",
    "08": "August",
    "9": "September",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
'''
month= input("Enter the month number (e.g., for January, enter 1).""\n")
#m_ = months.get(input())
print(month)   #This will get the current month

ElecPlan = input("Enter your electricity plan (EFIR or EFLR).""\n")

Efixed = 0.0836
Efixedii = 0.0941
Efloat = 0.0911
ElecValue =int(input("Enter the amounth of electricity you used in month "+month+" (in kWh).\n"))


if ElecPlan == "EFIR":
    if (ElecValue <= 1000):
        ElecAns=(Efixed * ElecValue)
    else: 
        ElecAns= (1000 * Efixed) + (Efixedii * (ElecValue-1000))
else:
    ElecPlan == "EFLR"
    if ElecValue <1000:
        ElecAns=(Efloat * ElecValue)
    else:
        ElecAns= (ElecValue * Efixedii)


#Gas plan 

GasPlan = input("Enter your gas plan (GFIR or GFLR).""\n")
Gfixed = 0.0456
Gfloating = 0.0393
Gfixedii = 0.0589
GasValue =  int(input("Enter the amount of gas you used in month "+month+" (in GJ).\n"))
if GasPlan == "GFIR":
    if (GasValue <= 950):
        GasAns=(Gfixed * GasValue)
    else: 
        GasAns= (950 * Gfixed) + (Gfixedii * (GasValue - 950))
elif GasPlan == "GFLR":
    GasAns=Gfloating * GasValue 



'''else:
    GasPlan == "GFLR"
    if GasValue <950:
        GasAns=(Gfloating * GasValue)
    else:
        GasAns= (GasValue * Gfixedii)
'''

T1= (ElecAns)
T2= (GasAns)
T3= (T1 + T2 + 120.62 + 1.32)
#print("Your total before tax is")
#print(T3)

# Provincial Tax

Prov = input("Enter the abbreviation for your province of residence (two letters.)""\n")
'''   
if Prov == "AB":
    UncleSam= 0.05 * T3 
elif Prov == "BC":
    UncleSam= 0.05 * T3 
elif Prov == "MB":
    UncleSam= 0.05 * T3 
elif Prov == "NT":
    UncleSam= 0.05 * T3 
elif Prov == "NU":
    UncleSam= 0.05 * T3 
elif Prov == "QC":
    UncleSam= 0.05 * T3
elif Prov == "SK":
    UncleSam= 0.05 * T3 
elif Prov == "YT":
    UncleSam= 0.05 * T3 
elif Prov == "ON":
    UncleSam= 0.13 * T3 
elif Prov == "NB":
    UncleSam= 0.15 * T3 
elif Prov == "NL":
    UncleSam= 0.15 * T3 
elif Prov == "NS":
    UncleSam= 0.15 * T3 
elif Prov == "PE":
    UncleSam= 0.15 * T3 
else:
    print("Something aight right")
'''
if Prov == "AB" or "BC"or "MB"or "NT" or "NU" or "QC" or "SK" or"YT":
    UncleSam = 0.05 * T3
elif Prov == "ON":
    UncleSam = 0.13 * T3
elif Prov == "NB" or "NL" or "NS" or "PE":
    UncleSam = 0.15 * T3
else:
    print("What a blunder")
      
Final= (UncleSam + T3)

print("Thank you! Your total amount due is:\n$",(round(Final,2)))


