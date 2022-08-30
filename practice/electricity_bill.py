TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def electricity_bil1(price_kwh, kwh, days):
    price = price_kwh * kwh * days
    return price

def main():
    # 选择模块
    choose = input('Please select the corresponding electricity price: (input 1 or 2)') # 请选择电价
    if choose == '1':
        price_kwh = TARIFF_11
    elif choose == '2':
        price_kwh = TARIFF_31
    else:
        return -1
    # 输入信息
    kwh = int(input('Please enter the daily power consumption: '))
    days = int(input('Please enter the days of power consumption:'))
    print('The total electricity price is:',electricity_bil1(price_kwh, kwh, days),'cents')
main()