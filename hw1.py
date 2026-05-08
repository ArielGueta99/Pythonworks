import math

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
    a = i[0]
    b = i[1]
    n = i[2]
    print("----------------------")
    print(f"Current case: {i}")
    print(f"Original fraction: {a}/{b}")
    gcd = math.gcd(i[0], i[1])  # also returns 1 if numerator is 0
    if gcd == 1:
        print(f"Reduced fraction: {a}/{b}")
    else:
        print(f"Reduced fraction: {int(a/gcd)}/{int(b/gcd)}")

    # stopped here!
    for k in range(n + 1):
        print(f"this is n: {n} this is k: {k} then n choose k is: {math.comb(n, k)}")
    # print(f"Symbolic binomial expansion: {expansion}")

# summary
print("========================")
print("Summary")
print("========================")

print(f"valid cases: {validCases}")
print(f"invalid cases: {invalidCases}")
