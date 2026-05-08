numOfCases = int(input("How many cases would you like to enter? "))
validCases = []
invalidCases = []

# input validation
for currentCase in range(1, numOfCases + 1):

    while True:
        print(f"Case number {currentCase}")
        userInputRaw = input("Enter: numerator denominator power -> ")
        userInputSplit = userInputRaw.split()

        try:
            a, b, n = map(int, userInputSplit)
            if int(b) == 0:
                print("Error: denominator cannot be zero")
                invalidCases.append((a, b, n))
                break
            if n < 0:
                print("Error: power must be non-negative")
                invalidCases.append((a, b, n))
                break

        except ValueError:
            print("Error: all values must be integers")
            invalidCases.append(userInputRaw)
            break

        validCases.append((a, b, n))
        break

# calculations
for i in validCases:
    print("----------------------")
    print(f"Current case: {i}")

# summary
print("========================")
print("Summary")
print("========================")

print(f"valid cases: {validCases}")
print(f"invalid cases: {invalidCases}")
