from decimal import Decimal


# Initialize denominator
k = Decimal(1)

# Initialize sum
s = 0

for i in range(1000000):

    # even index elements are positive
    if i % 2 == 0:
        s += Decimal(4)/k
    else:
        # odd index elements are negative
        s -= Decimal(4)/k

    # denominator is odd
    k += 2

print(s)
