# >>> (a := 23)
# 23


# ---------------------------------------------------------------------------------------


def distance(a, b):
    return abs(a-b)

if (d := distance(2, 5)) < 4:
    print(f"distance {d} is smaller than 4.")

a = 0
b = 8

while (d := distance(a,b)) > 3:
    print(f"the distance between a and b is {d}")
    a += 1


# ---------------------------------------------------------------------------------------


names = ["Olivia", "Emma", "Sophia", "Isabella", "Mia"]

if any("mm" in (witness := name) for name in names):
    print(f"{witness} contains 'mm'")

if all("i" in (counter_example := name) for name in names):
    print(f"{counter_example} does not contain 'i'")
