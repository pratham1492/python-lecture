print("welcome to the pattern generator and number analyzer ")

while(True):
    print("select an option:")
    print("1.generate a pattern :")
    print("2.analyze a number :")
    print("3.exit:")

    user = int(input("entre a number "))

    if user ==1: 
        break  


    if user ==1:
        n = int(input("enter a number "))
        for i in range(n):
            for j in range(0,n):
                print("*")


