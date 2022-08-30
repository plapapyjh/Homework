def generate_star():
    # 输入需要输出几行
    count = int(input("line number; "))
    row = 1
    # 行循环
    while row <= count:
        col = 1
        # 输出行号
        print(row, end=" ")
        # 列循环
        while col <= row:
            # 设置end不换行
            print("*", end=" ")
            col += 1
        # 换行
        print("")
        row += 1
generate_star()