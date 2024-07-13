stringHours = input("Enter Hours: ")
stringRate = input("Enter Rate: ")
try:
    floatingHours = float(stringHours)
    floatingRate = float(stringRate)
except: 
    print("Enter a numeric value !")
    quit()

if floatingHours > 40: 
    regular = floatingRate * floatingHours
    overtimePay = (floatingHours - 40.0) * (floatingRate * 0.5)
    xp = regular + overtimePay
else: 
    xp = floatingHours * floatingRate

print("Pay:",xp)