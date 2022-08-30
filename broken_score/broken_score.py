score = float ( input ("score =") )
if 0<=score<50:
    print("Bad")
elif 50<=score<90:
    print("Pass")
elif 90<=score<=100:
    print("Excellent")
else:
    print("Please check the input!")