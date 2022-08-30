sales = float(input("Enter sales：$"))
bonus = 0  # bonus
if sales >= 0:
    if sales <= 1000:
        bonus = sales * 0.1
        print('A bonus of $%d shall be paid' % bonus)
    elif sales >= 1000:
        bonus = sales * 0.15
        print('A bonus of $%d shall be paid' % bonus)
else:
   print("Please check the input!")