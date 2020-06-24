#!/usr/bin/env python3

# -- Data Stream Configuration -- #

hgSpeeds = []
lgSpeeds = []
cSpeeds = []

recordedSpeeds = []

possibleCategories = ["H", "L", "C"]

# Start Taking The Data Stream

receiveStream = 1

while receiveStream == 1:

    current_input = str(input("Enter Vehicle's Category and Speed: "))

    if current_input == "END":
        receiveStream = 0
    else:

        vehicleCategory = current_input[:1]
        if vehicleCategory not in possibleCategories:
            print("Error: Vehicle Category Does Not Exist!")
        else:
            try:
                vehicleSpeed = int(current_input[1:])
                recordedSpeeds.append(vehicleCategory + str(vehicleSpeed))

                # Place each reading into 1 of 3 arrays to understand how many of each vehicle category has passed

                if vehicleCategory == "C":
                    cSpeeds.append(vehicleSpeed)
                elif vehicleCategory == "H":
                    hgSpeeds.append(vehicleSpeed)
                elif vehicleCategory == "L":
                    lgSpeeds.append(vehicleSpeed)
            except ValueError:
                print("Error: Could not convert speed to integer")

# Print Results Of The Data Stream

print("\n" + "\n" + "================")
print("====READINGS====" + "\n" + "\n")

for i in recordedSpeeds:
    print("Next Reading: " + i.__str__())

# Multiplier is used to calculate the KMH by multiplying the below value

kmhMultiplier = 1.60934

# Calculating Statistics

allSpeeds = []      # This array is used to hold the speeds of each passing vehicle.

for i in recordedSpeeds:
    allSpeeds.append(int(i[1:]))

print("\n" + "\n" + "================")
print("===STATISTICS===" + "\n")


print("Number of Vehicles: " + len(allSpeeds).__str__())

# Using the arrays made above, I know how many of each category using the length of each array
# Calculating the percentage of vehicle category by dividing by the total number of cars and multiplying by 100
print("Number of Heavy Goods: " + len(hgSpeeds).__str__() + "("+round(len(hgSpeeds)/len(allSpeeds) * 100).__str__()+"%)")
print("Number of Light Goods: " + len(lgSpeeds).__str__() + "("+round(len(lgSpeeds)/len(allSpeeds) * 100).__str__()+"%)")
print("Number of Private Cars: " + len(cSpeeds).__str__() + "("+round(len(cSpeeds)/len(allSpeeds) * 100).__str__()+"%) \n")

print("Highest Speed Seen: " + max(allSpeeds).__str__() + " MPH" + " (" + round(
            max(allSpeeds) * kmhMultiplier).__str__() + " KMH)")
print("Lowest Speed Seen: " + min(allSpeeds).__str__() + " MPH" + " (" + round(
            min(allSpeeds) * kmhMultiplier).__str__() + " KMH)")

# Calculating Averages

avgMPH = round(sum(allSpeeds) / len(allSpeeds))
avgKMH = round(avgMPH * kmhMultiplier)
print("Average Speed Seen: " + avgMPH.__str__() + " MPH" + " (" + avgKMH.__str__() + " KMH)" + "\n")

# Speed violations

speedViolation = 0

for i in allSpeeds:
    if i > 50:
        speedViolation = speedViolation + 1

# Calculate Percentage of Violations

percentage = round(speedViolation / len(allSpeeds) * 100)

print("Speed Limit Violations: " + speedViolation.__str__() + " (" + percentage.__str__() + "%)")
