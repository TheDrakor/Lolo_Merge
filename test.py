arr = [1,2,3,4,5,6,7,8,9]

for a in arr:
    if a >= 5:
        for r in range(1,6):
            print(a*r, end = "\t")
    print("")
