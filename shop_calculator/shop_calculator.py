amount = int(input("Please enter the quantity of purchased goods：")) #输入购买商品的数量
price = float(input("Please enter the commodity unit price：")) #输入商品单价
total = amount*price
if  0 <= total <= 100:
    rate = 0
elif 100 <total:
    rate = 0.1
else:
    print("Please check your input!")
total = float(price * amount * (1 - rate))
print("Amount payable by customers：%.2f" % total) #顾客应付金额