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
            # a , b, n must be exactly 3 digits.
            if len(userInputSplit)!=3:
                print("Error: there must be exactly 3 values")
                invalidCases.append(userInputRaw)
                break
            a, b, n = map(int, userInputSplit)
            # b shouldn't be zero
            if b == 0:
                print("Error: denominator cannot be zero")
                invalidCases.append((a, b, n))
                break
            # n should be int already, if it gives out False, it's less than zero.
            if not n:
                print("Error: power must be non-negative")
                invalidCases.append((a, b, n))
                break
        #exception from map, values mst be ints
        except ValueError:
            print("Error: all values must be integers.")
            invalidCases.append(userInputRaw)
            break

        validCases.append((a, b, n))
        break
