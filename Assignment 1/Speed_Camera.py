#!/usr/bin/env python3

# -- MANUALLY ENTER THE DATA STREAM -- #

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
            except ValueError:
                print("Error: Could not convert speed to integer")



# Print Results

print("")
print("")
print("==================")
print("====Readings====")
print("")
print("")
for i in recordedSpeeds:
    print("Next Reading: " + i.__str__())



# Convert to KMH

kmhMuliplier = 1.60934

# Calculating Statisics

allSpeeds = []

for i in recordedSpeeds:
    allSpeeds.append(int(i[1:]))

print("")
print("")
print("================")
print("===STATISTICS===")
print("")


print("Number of Vehicles: " + len(allSpeeds).__str__())
print("Highest Speed Seen: " + max(allSpeeds).__str__() + " MPH" + " (" + (max(allSpeeds) * kmhMuliplier).__str__() + " KMH)")
print("Lowest Speed Seen: " + min(allSpeeds).__str__() + " MPH" + " (" + (min(allSpeeds) * kmhMuliplier).__str__() + " KMH)")

print("")

avgMPH = sum(allSpeeds) / len(allSpeeds)
avgKMH = avgMPH * kmhMuliplier
print("Average Speed Seen: " + avgMPH.__str__() + " MPH" + " (" + avgKMH.__str__() + " KMH)" + "\n")

print("")

# Speed violations

speedViolation = 0

for i in allSpeeds:
    if i > 50:
        speedViolation = speedViolation + 1

# Calculate Percentage of Violations

percentage = speedViolation / len(allSpeeds) * 100

print("Speed Limit Violations: " + speedViolation.__str__() + " (" + percentage.__str__() + "%)")
