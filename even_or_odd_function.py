def oddoreven(a):
    if(a==0):
        print(a," is neither even nor odd")
    elif(a%2==0):
        print(a," is even")
    else:
        print(a," is odd")


a=int(input("enter number to check oddoreven"))
oddoreven(a)
