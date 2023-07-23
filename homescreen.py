while True:
    print("\nTo choose an option, type either 'cosdegree', 'cosradian', 'sindegree', 'sinradian', or 'unitcircle' \n")
    choose = input("~ Would you like to practice identifying values of:\n cosine in degrees, cosine in radians, sine in degrees, or sine in radians?\n Or, would you like to practice filling in the unit circle? \n")
    if choose == "cosdegree":
        import cosdegrees
    elif choose == "cosradian":
        import cosradians
    elif choose == "sindegree":
        import sindegrees
    elif choose == "sinradian":
        import sinradians
    elif choose == "unitcircle":
        import unitcircle
    else:
        print ("~ try retyping ~")