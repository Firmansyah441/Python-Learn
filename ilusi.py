import math

for y in range(-12, 12):
    for x in range(-40, 40):
        d = math.sqrt(x**2 + y**2)
        c = " .:-=+*#%@"
        print(c[int(d) % len(c)], end="")
    print()
