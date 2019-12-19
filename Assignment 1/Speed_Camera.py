#!/usr/bin/env python3

# -- MANUALLY ENTER THE DATA STREAM -- #


h = int(input('Enter speed of Heavy Goods Vehicle: '))
l = int (input ('Enter speed of Light Goods Vehicle: '))
c = int (input ('Enter the speed of Car: '))
c2 = int (input ('Enter the speed of Second Car: '))

# -- -- -- -- -- -- -- -- -- -- -- -- #


heavySpeeds = [h]
lightSpeeds = [l]
carSpeeds = [c, c2]

for i in heavySpeeds:
    print("Next Reading: H" + i.__str__())

for i in lightSpeeds:
    print("Next Reading: L" + i.__str__())

for i in carSpeeds:
    print("Next Reading: C" + i.__str__())

print ( "Next Reading: end\n")

# Convert to KMH

kmhMuliplier = 1.60934


# Calculate Values Between All Vehicles

allVehicles = [h, l, c, c2]

print ( "Number of Vehicles: " + len(allVehicles).__str__() + " MPH" + " (" + (len(allVehicles)*kmhMuliplier).__str__() + " KMH)")
print ( "Highest Speed Seen: " + max(allVehicles).__str__() + " MPH" + " (" + (max(allVehicles)*kmhMuliplier).__str__() + " KMH)")
print ( "Lowest Speed Seen: " + min(allVehicles).__str__() + " MPH" + " (" + (min(allVehicles)*kmhMuliplier).__str__() + " KMH)")

avgMPH = sum(allVehicles)/len(allVehicles)
avgKMH = avgMPH*kmhMuliplier
print ( "Average Speed Seen: " + avgMPH.__str__() + " MPH" + " (" + avgKMH.__str__() + " KMH)" + "\n")

# Calculating Speed Limit Violation

speedViolation = 0

for i in allVehicles:
    if i > 50:
        speedViolation = speedViolation + 1

# Calculate Percentage of Violations

percentage = speedViolation / len(allVehicles) * 100

print ( "Speed Limit Violations: " + speedViolation.__str__() + " (" + percentage.__str__() + "%)")




