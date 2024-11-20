row = int(input("Enter the no. of row: "))
number=0

for i in range(row,0,-1):
    for j in range(0, i):
        print("* ", end=' ')
    print()