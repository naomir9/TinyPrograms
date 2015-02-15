# Produces multiplication tables 1- 12

for x in range(1,13):
    for y in range(1,13):
        print("%2d x %2d = %3d \t" % (x, y, x*y), end='')
    print()