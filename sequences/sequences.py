x = int(input("x= ")) #开始数字
y = int(input("y= ")) #结束数字
odd = range(x, y + 1, 2)
even = range(x + 1, y + 1, 2)
def squares():
    a = list(range(x, y, 1))
    all = []
    for i in a:
        i = i * i
        all.append(i)
    return all
print("odd:",list(odd))
print("even:",list(even))
print("The squares of all numbers are:",squares())