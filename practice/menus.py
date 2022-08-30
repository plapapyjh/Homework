choice=0
while True:
    print("""          ---------------Menu--------------
          1.    H . . . . . . . . . .hello
          2.    G . . . . . . . . . .googbye
          3.    Q . . . . . . . . . .quit
          4.    Other things . . . . reenter
          _________________________________ """)
    choice = input("choice = ")
    if choice == "H":
        print("hello")
        continue
    elif choice == "G":
        print("goodbye")
        continue
    elif choice == "Q":
        break
    else:
        print("Please check your input!")
        continue